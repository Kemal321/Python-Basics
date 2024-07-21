'''
Yapılmak istenen: ATM Uygulaması
Gereksinimler:
Giriş Sistemi: Kullanıcıdan kullanıcı adı ve PIN kodu isteyin. Basit bir sözlük (dict) kullanarak kullanıcı adı ve
PIN kodlarını saklayın.
İşlemler Menüsü: Giriş yaptıktan sonra kullanıcının yapabileceği işlemler:
        Bakiye Sorgulama
        Para Yatırma
        Para Çekme
        Hesap Bilgilerini Güncelleme
        Çıkış Yapma
Veritabanı: Kullanıcı bilgilerini, hesap bakiyelerini ve işlem geçmişini saklamak için bir sözlük (dict) kullanın.
Metodlar:
Kullanıcı girişini kontrol eden metod
Bakiye sorgulama, para yatırma ve çekme işlemlerini gerçekleştiren metodlar
Hesap bilgilerini güncelleyen metod
Menü ve işlem seçimlerini yöneten metod
'''
bugün = "13.06.2024"
print("""
***************MERHABA A-BANK'A HOŞ GELDİNİZ***********************
            LÜTFEN KARTINIZI CİHAZA YERLEŞTİRİNİZ
""")

users = {"kullanıcı1":{
    "İsim": "Kemalettin",
    "Soyisim": "KARA",
    "Şifre": 123,
    "Hesap Numarası": 123456,
    "Bakiye": 6000,
    "Borç": 3000,
    "Borç Kesim Tarihi": "28/0x"
},
         "kullanıcı2":{
    "İsim": "Ahmet",
    "Soyisim": "YILMAZ",
    "Şifre": 1234,
    "Hesap Numarası": 123456,
    "Bakiye": 6000,
    "Borç": 3000,
    "Borç Kesim Tarihi": "28/0x"
}}

takılanKart = dict(users["kullanıcı1"]) # varsayarak ilerliyoruz çünkü atm makinemiz yok

count = 2
for i in range(0,3):
    şifre = int(input("Lütfen Kart Şifrenizi Giriniz: "))
    if şifre == takılanKart.get("Şifre"):
        print("""
        GİRİŞ BAŞARILI YAPMAK İSTEDİĞİNİZ İŞLEMLERİ İŞLEM MENÜSÜNDEN SEÇEBİLİRSİNİZ
        İŞLEM MENÜSÜ:
            [1] Bakiye Sorgulama
            [2] Para Yatırma
            [3] Para Çekme
            [4] Hesap Bilgilerini Güncelleme
            [Q-q] Çıkış Yapma

""")
        sec = input("Seçilecek menü kodu: ")
        break
    elif şifre != takılanKart.get("Şifre") and count != 0:
        print("ŞİFRENİZ HATALIDIR LÜTFEN TEKRAR DENEYİNİZ\n KALAN HAKKINIZ {}".format(count))
        count -=1
    elif şifre != takılanKart.get("Şifre") and count == 0:
        print("ÇOK FAZLA HATALI GİRİŞ. BU KART BLOKE OLMUŞTUR\n       LÜTFEN EN YAKIN ŞUBEYE GİDİNİZ")
        exit()

if sec == "1":
    print(f"""
    SEÇİLEN İŞLEM BAKİYE SORGULAMA
    MEVCUT BAKİYENİZ: {takılanKart.get("Bakiye")}
""")
elif sec == "2":
    print(f"""
    SEÇİLEN İŞLEM PARA YATIRMA 
    MEVCUT BAKİYENİZ: {takılanKart.get("Bakiye")}
""")
    yatırılacakTutar = int(input("LÜTFEN YATIRMAK İSTEDİĞİNİZ TUTARI GİRİNİZ: "))
    takılanKart["Bakiye"] += yatırılacakTutar 
    print(f"Tarih: {bugün}\n GÜNCEL BAKİYENİZ: {takılanKart.get("Bakiye")} ")
elif sec == "3":
    print(f"""
    SEÇİLEN İŞLEM PARA ÇEKME 
    MEVCUT BAKİYENİZ: {takılanKart.get("Bakiye")}
""")
    çekilecekPara = int(input("LÜTFEN ÇEKMEK İSTEDİĞİNİZ MİKTARI GİRİNİZ: "))
    takılanKart["Bakiye"] -= çekilecekPara
    print("{} PARA ÇEKİLMİŞTİR SON DURUMDAKİ BAKİYE {} KONTROL ETMEDEN ALMAYI UNUTMAYINIZ".format(çekilecekPara,(takılanKart.get("Bakiye") - çekilecekPara)))
elif sec == "4":
    print("YAPILAN İŞLEMLER KAYDEDİLMİŞTİR HESAP BİLGİLERİ GÜNCELLENMİŞTİR")
elif sec == "Q" or sec == "q":
    print("KARTINIZI ALMAYI UNUTMAYIN BİZİ TERCİH ETTİĞİNİZ İÇİN TEŞEKKÜR EDERİZ")
else:
    print("HATALI İŞLEM SEÇTİNİZ LÜTFEN DAHA SONRA TEKRAR DENEYİNİZ")
    exit()













