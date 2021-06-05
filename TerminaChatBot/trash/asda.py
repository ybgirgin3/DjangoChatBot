from readdb_trash import main as dbmain
from pprint import pprint

#privKey = "810e4a9a"
#ind = 2
#acc = dbmain("register_customuser")
#acc = dbmain("root_arizakaydi")
#priv = [i[-1] for i in acc]

# listelerin alayını dönüyor
#pprint(acc)

"""
for user in acc:
    if ind in user:
        print(user)
"""

"""
for err in acc:
    if err[-1] == ind:
        print(err)
"""


# emailden kullanıcı bulma
"""
email1 = "berkay@gmail.com"
email2 = "arel@gmail.com"

for user in acc:
    if email2 in user[-2]:
        print(user)

"""

# veritabanına eleman ekleme

"""
import sqlite3

vt = sqlite3.connect('vt.sqlite')
im = vt.cursor()


#değer_gir = #INSERT INTO personel VALUES ('Fırat', 'Özgül', 'Adana')

#im.execute(tablo_yap)
#im.execute(değer_gir)
"""

user_index = 2
item_index = len([item for item in dbmain("root_arizakaydi", fetch=True)]) + 1
print(item_index)
item_name = "pythondan eklenen hata"


insert = dbmain("root_arizakaydi",
                send=True,
                user_index=user_index,
                item_name=item_name,
                item_index=item_index)
print(insert)

#item for item in dbmain("root_arizakaydi") + 1

"""
for item in dbmain("root_arizakaydi", fetch=True):
    print(item[1])
"""

"""
from termcolor import colored
    
usersItem = dbmain("root_arizakaydi", fetch=True)
print("sizin tarafınızdan kaydedilmiş tüm bildirimler: ")
for item in usersItem:
    print(colored(item[1], "blue"))

"""