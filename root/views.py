from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# veritabanından verileri çek ve ekrana yazdır
from .models import ArizaKaydi, Item

# formlar için import
from .forms import ArizaKaydiOlustur
# Create your views here.

# veri tabanı içindeki elemanları
# url kısmına verilecek olan integer değerlere göre list.html
# içinde yazdır
# /home/1 ya da /home/2 gibi
def index(response, id):
    ls = ArizaKaydi.objects.get(id=id)

    if ls in response.user.ariza.all():
        # herhangi bir girdi var mı diye kontrol et
        if response.method == "POST":
            print(response.POST)
            # save butonuna basıldığından;
            # save butonu sadece tik butonunu kontrol ediyor
            # gereksiz olduğu düşünüldüğünde silinebilir
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            # eğer save butonu yerine yeni öğe butonuna basılırsa;
            # yeni öğe butonu veritabanına yeni bir öğe eklemeye yarıyor
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text = txt, complete = False)
                else:
                    print("invalid")

        return render(response, "root/list.html", {"ls": ls})
    return render(response, "root/home.html", {})

# sitenin anasayfasını renderla
# NOTE: direk olarak login kısmına gitse daha iyi olur
# NOTE: login kısmının yüklenmesi sıkıntılı olduğundan dolayı
# anasayfanın üzerinde eğer giriş yapılmamışsa
#
def home(response):
    import random
    # fiyatları
    price = [ round(random.uniform(1000, 10000), 2) for _ in range(0,24)]
    return render(response, "root/home.html", {"price": price})

# veri tabanına yeni bir arıza kaydı girmek için
# gerekli olan bilgileri create.html içinden al
def create(response):
    # eğer create.html sayfası içindeki alanlar boş değilse
    # response'un methodu 'post' olarak döner.
    # eğer method post ise
    if response.method == "POST":
        # form içindeki tüm bilgiyi form değişkenine ata
        form = ArizaKaydiOlustur(response.POST)

        # eğer değişkenlerin içi boş değilse
        if form.is_valid():
            # girilen bilgiler veritabanına kaydet
            name = form.cleaned_data['name']
            t = ArizaKaydi(name=name)
            t.save()
            response.user.ariza.add(t)

        # kaydettikten sonra direk olarak kaydı göster
        return HttpResponseRedirect("/%i" % t.id)

    else:
        # boş bir form oluşturuyor ve create.html içine yolluyor
        form = ArizaKaydiOlustur()
    return render(response, "root/create.html", {"form": form})



#from .models import Events yerine Item kullan
# hoca buna gerek kalmadığını söyledi
# gg wp
def all_events(response):
    user_list = ArizaKaydi.objects.all()
    return render(response, "root/events.html", {"user_list": user_list})


def view(response):
    return render(response, "root/view.html")

def about(response):
    return render(response, "root/about.html")
