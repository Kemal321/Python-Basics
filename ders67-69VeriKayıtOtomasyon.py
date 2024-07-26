import re
import time

class Kayıt:
    def __init__(self, programad):
        self.programad = programad
        self.dongu = True
    def program(self):
        secim = self.menu()
        if secim == '1':
            print("Kayıt ekleme ekranına yönlendiriliyorsunuz ....")
            time.sleep(3)
            self.kayıtEkle()
        elif secim == '2':
            print("Kayıt Sil ekranına yönlendiriliyorsunuz ....")
            time.sleep(3)
            self.kayıtSil()
        elif secim == '3':
            print("Kayıt Oku ekranına yönlendiriliyorsunuz ....")
            time.sleep(3)
            self.kayıtOku()
        elif secim == '4':
            print("Sistemden çıkılıuyor....")
            time.sleep(3)
            self.cıkıs()

    def menu(self):
        def kontrol(secim):
            if re.search("[^1-4]",secim):
                raise Exception("Lütfen 1 ile 4 arasında bir seçim giriniz!!!")
            elif (len(secim)>1):
                raise Exception("Lütfen 1  ile 4 arasında sayı giriniz!!!")
        while True:
            try:
                secim=input("Merhaba, {} Sistemine hoş geldiniz.\nLütfen yapmak istediğiniz işlemi seçiniz.\n[1]-Kayıt Ekle\n[2]-Kayıt Sil\n[3]-Kayıt Oku\n[4]-Çıkış\n\n".format(Sistem.programad))
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(3)
            else:
                break
        return secim
    def kayıtEkle(self):
        def kontrolAd(Ad):
            if Ad.isalpha() == False:
                raise Exception("Adınızda sadece alfabetik karakterler olmalıdır....")
        while True:
            try:
                Ad = input("Adınız: ")
                kontrolAd(Ad)
            except Exception as adHatası:
                print(adHatası)
                time.sleep(3)
            else:
                break
        def kontrolSoyad(Soyad):
            if Soyad.isalpha() == False:
                raise Exception("Soyadınızda sadece alfabetik karakterler olmalıdır....")
        while True:
            try:
                Soyad = input("Soyadınız: ")
                kontrolAd(Ad)
            except Exception as soyadHatası:
                print(soyadHatası)
                time.sleep(3)
            else:
                break

        def kontrolYas(Yas):
            if Yas.isdigit() == False:
                raise Exception("Yaşınız sadece rakamlardan oluşmalıdır....")
        while True:
            try:
                Yas = input("Yaşınız: ")
                kontrolYas(Yas)
            except Exception as yasHatası:
                print(yasHatası)
                time.sleep(3)
            else:
                break

        def kontrolTc(Tc):
            if Tc.isdigit() == False:
                raise Exception("Tc sadece nümerik karakterler olmalıdır....")
            elif len(Tc) != 11:
                raise Exception("Tc niz 11 karakterden oluşmalıdır...")
        while True:
            try:
                Tc = input("Tc: ")
                kontrolTc(Tc)
            except Exception as tcHatası:
                print(tcHatası)
                time.sleep(3)
            else:
                break
        def kontrolMail(Mail):
            if not re.search("@" and ".com",Mail):
                raise Exception("Lütfen geçerli bir mail giriniz....")
        while True:
            try:
                Mail = input("Mail: ")
                kontrolMail(Mail)
            except Exception as mailHatası:
                print(mailHatası)
                time.sleep(3)
            else:
                break
        
        with open("C:/Users/Kemalettin/Desktop/Anlaşılır Ekonomi/Python/database.txt","r",encoding="utf-8") as Dosya:
            satirSayisi = Dosya.readlines()
        if len(satirSayisi) == 0:
            Id = 1
        else:
            with open("C:/Users/Kemalettin/Desktop/Anlaşılır Ekonomi/Python/database.txt","r",encoding="utf-8") as Dosya:
                Id = int(Dosya.readlines()[-1].split("-")[0])+1
        with open("C:/Users/Kemalettin/Desktop/Anlaşılır Ekonomi/Python/database.txt","a+",encoding="utf-8") as Dosya:
            Dosya.write("{}-{} {} {} {} {}".format(Id,Ad,Soyad,Yas,Tc,Mail))
            print("Veriler işlenmiştir....")
        self.menuDon()
    def kayıtSil(self):
        silinecekId = input("Silinecek Id yi giriniz:")
        with open("C:/Users/Kemalettin/Desktop/Anlaşılır Ekonomi/Python/database.txt","r",encoding="utf-8") as Dosya:
            liste = []
            liste2 = Dosya.readlines()
            for i in range(0, len(liste2)):
                liste.append(liste2[i].split("-")[0])

        del liste2[liste.index(silinecekId)]

        with open("C:/Users/Kemalettin/Desktop/Anlaşılır Ekonomi/Python/database.txt","w+",encoding="utf-8") as YeniDosya:
            for i in liste2:
                YeniDosya.write(i)
            print("Kayır siliniyor...")
            time.sleep(3)
            print("Kayıt silinmiştir...")
            self.menuDon()

    def kayıtOku(self):
        with open("C:/Users/Kemalettin/Desktop/Anlaşılır Ekonomi/Python/database.txt","r",encoding="utf-8") as Dosya:
            for i in Dosya:
                print(i)
            self.menuDon()
    def cıkıs(self):
        print("Otomasyondan çıkılıyor....")
        time.sleep(3)
        self.dongu = False
        exit()
    def menuDon(self):
        while True:
            x = input("Ana menüye dönmek için 6'ya, çıkmak için lütfen 5 e basınız....: ")
            if x == "6":
                print("Ana menüye dönülüyor")
                time.sleep(3)
                self.program()
                break
            elif x == "5":
                self.cıkıs()
                break
            else:
                print("Lütfen geçerli bir seçim yapınız: ")


Sistem = Kayıt("Kemalettin Otomasyon")
while True:
    Sistem.program()