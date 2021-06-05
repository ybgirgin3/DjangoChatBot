import random
import sys
from termcolor import colored
from readdb import main as dbmain

# terminale yazdırma renkleri
input_color = "yellow"
notr_color = "blue"
return_false_color = "red"
return_true_color = "green"

# selamlama
selamla = [
        "Merhaba",
        "Nasılsınız",
        "Hoşgeldiniz",
        "Selamlar",
        ]

# rastgele bir tane eleman seç
greet = random.choice(selamla)

def greetings() -> str:
    string = """
    {},

    Özdil Telekom resmi hizmet botuna hoşgeldiniz..
    Hizmete başlamadan önce doğrulama işleminin tamamlanması için hesap numaranızı giriniz

    Hizmet numaranızı unuttuysanız _____ : 9
    Çıkış için _________________________ : -1

    Eğer hesap numaranız yoksa {} linki takip ederek sitemize gidebilir ve üye olabilirsiniz


    """.format(greet, colored("http://127.0.0.1:8000/register/", notr_color))
    return string

def process() -> int:
    # NOTE:
    # ana menü

    print("""
    Size nasıl yardımcı olabilirim ?

        arıza bildirimlerim ____ : 1
        tüm arızalar ___________ : 2
        yeni arıza bildir ______ : 3


        çıkış __________________: -1


    """)
    opt = int(input(colored("seçim: ", input_color)))
    return opt

##### KULLANICI HESAP İŞLEMLERİ ######
def is_user_exist(data: str) -> str:
    # NOTE:
    # kullanıcı "tüm" kayıtlı bilgileri veritabanından bulup ekrana yazdır -> veritabanı bağlantısı içerir
    # aktif olabilmesi için giriş yapılması gerekir

    acc = dbmain("register_customuser")

    for user in acc:
        if data in user:
            print(colored("Kullanıcı doğrulandı", return_true_color))
            print("""
               Kullanıcı Adı: {},
               Kullanıcı Emaili: {},
               Hesap Numarası: {}
               """.format(user[4], user[10], user[-1]))
               # kullanıcının kaydolma indeksini dön
            return user[0]

def learnAboutUser(email) -> str:
    # NOTE:
    # veritabanından kullanıcını privateKey'ini verir
    # kullanıcının giriş yapmak için hesap numarasını hatırlamazsa girmesi gerekie
    # aktif olabilmesi için giriş yapılmasına gerek yok

    acc = dbmain("register_customuser")

    for user in acc:
        if email in user[-2]:
            string = f"{colored(user[4], 'yellow')} isimli kullanıcı için kayıtlı hesap no: {colored(user[-1], 'yellow')}"
            return string

def listingFromDB(ind = None) -> str:
    # NOTE:
    # kayıtlı arıza bildirimlerini listeler
    # eğer "ind" değişkeni boş değer değilse

    usersItem = dbmain("root_arizakaydi")
    # ind none ise
    if ind is None:
        print("tüm kullanıcılar tarafından kaydedilmiş olan bildirimler: ")
        for item in usersItem:
            print(colored(item[1], notr_color))

    if ind is not None:
        #userItem = dbmain("root_arizakaydi")
        for item in usersItem:
            print("sizin tarafınızdan kaydedilmiş tüm bildirimler: ")
            if ind in item:
                print(colored(item[1], notr_color))

if __name__ == '__main__':
    # ana menüyü göster
    # kullanıcıdan hesap no al
    # hesap no kontrol et
    # işlem menüsünü göster (while loop içinde)


    # hoşgeldin mesajı
    print(greetings())

    # hesap no
    privateKey = input(colored("hesap no: ", input_color))
    # hesap no eğer 9 veya -1 den ikisi de değilse
    if privateKey != "9" and privateKey != "-1":
        if userIndex := is_user_exist(privateKey) is not None:
            # process as a integer
            while True:
                opt = process()
                # veritabanındaki "benim" verilerimi listele
                # bu kısımda fonksiyondan return edip
                # burda yazdırma kısmı başarısız oluyor
                # çünkü tek bir eleman dönüyor
                if opt == 1:
                    listingFromDB(ind = userIndex)
                # veritabanındaki "tüm" verileri listele
                elif opt == 2:
                    listingFromDB()
                # yeni arıza ekle
                elif opt == 3:
                    print(colored("yeni bir arıza eklemek için 'http://127.0.0.1:8000/create/' linkini takip ederek arıza kayıt ekranımıza gidebilirsiniz ", return_true_color))
                    print("linkini takip edin")

                # çıkış yap
                elif opt == -1:
                    print("çıkış yapılıyor...")
                    sys.exit(0)


        else: print(colored("kullanıcı bulunamadı", return_false_color))

    # hesap numaramı bilmiyorum
    elif privateKey == "9":
        email = input("email adresinizi girin: ")
        if useremail := learnAboutUser(email):
            print(useremail)
        else:
            print(colored("kullanıcı bulunamadı", return_false_color))

    # çıkış yap
    elif privateKey == "-1":
        print("çıkış yapılıyor...")
        sys.exit(0)
