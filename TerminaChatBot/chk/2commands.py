# bot ile kullanıcı arasında geçecek olan konuşmalar
# kullanıcının sorduğu sorular arasında seçilecek olan kelimeler
# botun vereceği cevapları içeren listeler

# selamlama
greetings = [
        "Merhaba",
        "Nasılsınız",
        "Hoşgeldiniz",
        "Selamlar",
        ]

helper_commands = {
    # internet hataları
    'internet' : {
            "Modeminizi kapatıp açmayı deneyin",
            "Bilgisayarınıza bağlı olan ethernet kablosunu çıkarıp tekrardan takmayı deneyin",
            "Tarayıcınızdan Özdil Telekom kullanıcı arayüzüne girip santralden gelen bağlantı var mı kontrol edin"
            },

    # phone
    'telefon' : {
            "Sim kartınızı çıkarıp tekrar takın.",
            "Telefonunuzu kapatıp tekrar açın.",
            "Sim kartınızı farklı bir telefonda deneyiniz."
            }
}

