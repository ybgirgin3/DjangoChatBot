import random
import sys
from readdb import main as dbmain
from command_handler import main as chmain
from commands import greetings as gr


def greetings() -> str:
    string = """
    {},

    Özdil Telekom resmi hizmet botuna hoşgeldiniz..
    Hizmete başlamadan önce doğrulama işleminin tamamlanması için hesap numaranızı giriniz
    Hesap numaranızı bilmiyorsanız, "bilmiyorum" yazabilir veya "-1" tuşlayabilirsiniz.

    Eğer hesap numaranız yoksa {} linki takip ederek sitemize gidebilir ve üye olabilirsiniz


    """.format(random.choice(gr), "http://127.0.0.1:8000/register/")
    return string

def process() -> int:
    # NOTE:
    # ana menü
    # bu kısım girilen kelimeleri parçalıyıp içlerinden belirli kelimelere
    # göre rehber olacak
    print("""
    size nasıl yardımcı olabilirim ?

    örnek: internet hızım düştü, telefonum çekmiyor, internet kesildi
    """)
    opt = input("~: ")
    return opt

##### KULLANICI HESAP İŞLEMLERİ ######
def is_user_exist(data: str) -> str:
    # NOTE:
    # kullanıcı "tüm" kayıtlı bilgileri veritabanından bulup ekrana yazdır -> veritabanı bağlantısı içerir
    # aktif olabilmesi için giriş yapılması gerekir

    acc = dbmain("register_customuser")

    for user in acc:
        if data in user:
            print("Kullanıcı doğrulandı")
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
            string = f"{user[4]} isimli kullanıcı için kayıtlı hesap no: {user[-1]}"
            return string

def solutionPrinter(solutions: str) -> bool:
    # listedekilerden birtanesini yazdır
    # eğer sorun çözümledi derse
    # tekrarla yok eğer çözüldü derse
    # sistemi kapat

    def faultReport(solved: bool) -> bool:
        if solved:
            string = "Bunu duyduğuma sevindim bizi tercih ettiğiniz için teşekkür ederiz"
        elif not solved:
            string = """
                    Arıza kaydı bildiriminiz alınmıştır
                    Ekiplerimiz hatayı çözdüğünden mail yoluyla bildirim gelecektir
                    Bizi tercih ettiğiniz için teşekkür ederiz
                """
        return string


    sol = list(solutions)
    for i in range(len(sol)):
        print(sol[i])
        accept = input("bu yolları denemek sorununuzu çözdü mü ? [E/h]: ")
        if accept in ("E", "e"):
            print(faultReport(solved = True))
            return True

        elif accept in ("H", "h"):
            if i == (len(sol) - 1):
                createFaultReport(
                        user_id = userIndex
                        )
                print(faultReport(solved = False))
                return False
            else:
                pass


# create fault repot and save it to db
def createFaultReport(user_id):
    """
    python3 manage.py <name> <user_id> şeklinde bir çalıştırma yapacak
    ama BASE_DIR seçmem lazım
    """
    import os
    import sys
    sys.path.insert(0, "../")
    from ArizaKayit.settings import BASE_DIR

    print("""
          Ariza kaydiniz oluşturmak için sizde bilgiler alınacaktır
          """)

    # arıza kaydı için kullanıcıdan yazı al
    name = input("Ariza bildiriminiz: ")

    os.chdir(BASE_DIR)
    
    os.system(f"python3 manage.py chatbot_backend '{name}' {user_id}")





if __name__ == '__main__':
    # ana menüyü göster
    # kullanıcıdan hesap no al
    # hesap no kontrol et
    # işlem menüsünü göster (while loop içinde)


    # hoşgeldin mesajı
    print(greetings())

    # hesap no
    privateKey = input("hesap no: ")
    # cevap bilmiyorum ise kullanıcı bul
    if privateKey != "bilmiyorum" and privateKey != '-1':
        userIndex = is_user_exist(privateKey)
        if userIndex is not None:
            while True:
                # get option from user
                opt = process()

                # return point word in input
                pt = chmain(opt)

                # print solutions respectively -> dict
                # after printing one of the solutions
                # ask user if this solutions solved their problem
                is_solved = solutionPrinter(solutions =  pt)
                if is_solved:
                    break
                elif not is_solved:
                    # bu kısımda ariza kayıt işlemleri başlayacak
                    """ createFaultReport(
                        user_id = userIndex
                        )
                    """
                    break
    elif privateKey in ("bilmiyorum", "-1"):
        email = input("kurtarma email adresinizin giriniz: ")
        ret = learnAboutUser(email)
        print(ret)


