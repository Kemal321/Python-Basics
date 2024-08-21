# Gerekli kütüphanelerin yüklenmesi
import json
import re
import time
import random

class Site:
    def __init__(self):
        self.dongu = True
        self.veriler = self.verial()

    def program(self):
        secim = self.menu()

        if secim == "1":
            self.giris()
        if secim == "2":
            self.kayıtol()
        if secim == "3":
            self.cikis()

    def menu(self):
        def kontrol(secim):
            if re.search("[^1-3]",secim):
                raise Exception("Lütfen 1-3 arasında bir seçim yapınız...")
            elif len(secim) != 1:
                raise Exception("Lütfen sadece 1-3 arasında bir seçim yapınız...")
        while True:
            try:
                secim = input("Merhabalar, Kemalettin Kara'nın bloğuna hoşgeldiniz.\nLütfen yapmak istediğiniz işlemi seçiniz....\n\n[1]-Giriş\n[2]-Kayıt ol\n[3]-Çıkış\n\n----> ")
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(1.3)
            else:
                break
        return secim

    def giris(self):
        print("Giriş menüsüne yönlendiriliyorsunuz...")
        time.sleep(1.5)
        kullaniciAdi = input("Lütfen kullanıcı adını giriniz --> ")
        sifre = input("Lütfen şifrenizi giriniz --> ")
        print("Bilgiler kontrol ediliyor...")
        time.sleep(1.5)
        if self.girisKontrol(kullaniciAdi,sifre):
            self.girisBasarili()
        else:
            self.girisBasarisiz()

    def girisKontrol(self,kullaniciAdi,sifre):
        self.veriler = self.verial()
        try:
            for kullanici in self.veriler["Kullanıcılar"]:
                if kullanici["Kullanıcıadı"] == kullaniciAdi and kullanici["Şifre"] == sifre:
                    return True
        except KeyError:
            return False
        return False

    def girisBasarili(self):
        print("Blog sitesine hoş geldiniz...")
        time.sleep(0.7)
        self.dongu = False
        self.sonuc = False

    def girisBasarisiz(self):
        print("Lütfen bilgilerinizi kontrol ederek tekrar deneyiniz")
        time.sleep(0.7)
        self.menuDon()

    def kayıtol(self):
        def kontrolKa(kullaniciadi):
            if len(kullaniciadi) <8:
                raise Exception("Kullanıcı adınız 8 karakterden az olamaz")
        while True:
            try:
                kullaniciad = input("Lütfen kayıt olmak istediğiniz kullanıcı adını giriniz -->")
                kontrolKa(kullaniciad)
            except Exception as hataad:
                print(hataad)
                time.sleep(0.9)
            else:
                break
        def kontrolSi(sifre):
            if len(sifre) <8:
                raise Exception("Şifreniz 8 karakterden az olamaz")
            elif not re.search("[0-9]",sifre):
                raise Exception("Şifrenizde en az 1 tane rakam bulunmalıdır.")
            elif not re.search("[A-Z]",sifre):
                raise Exception("Şifrenizde en az 1 tane büyük harf bulunmalıdır.")
            elif not re.search("[a-z]",sifre):
                raise Exception("Şifrenizde en az 1 tane küçük harf bulunmalıdır.")
        while True:
            try:
                sifremiz = input("Lütfen kayıt olmak istediğiniz şifrenizi giriniz -->")
                kontrolSi(sifremiz)
            except Exception as sifrehatası:
                print(sifrehatası)
                time.sleep(0.9)
            else:
                break

        def kontrolMail(mail):
            if not re.search("@" and ".com", mail):
                raise Exception("Lütfen geçerli bir mail giriniz...")
        while True:
            try:
                mailim = input("Mail adresiniz --> ")
                kontrolMail(mailim)
            except Exception as hatamail:
                print(hatamail)
            else:
                break
        if self.kontrolKayit(kullaniciad,mailim):
            print("Bu kullanıcı adı sistemde kayıtlıdır veya mail sistemde kayıtlıdır.")
        else:
            aktivasyon = self.aktivasyonGonder()
            durum = self.aktivasyonKontrol(aktivasyon)
        while True:
            if durum == True:
                self.veriKaydet(kullaniciad,mailim,sifremiz)
                break
            else:
                input("Geçersiz aktivasyon kodu... Lütfen tekrar giriniz...\n... ")

    def kontrolKayit(self,kullaniciad,mail):
        self.veriler = self.verial()
        try:
            for kullanici in self.veriler["Kullanıcılar"]:
                if kullanici["Kullanıcıadı"] == kullaniciad and kullanici["Mail"] == mail:
                    return True
        except KeyError:
            return False
        return False
                
    def aktivasyonGonder(self):
        with open("C:/Users/Kemalettin/Desktop/aktivasyon.txt","w",encoding="utf-8") as dosya:
            aktivasyon = str(random.randint(10000,99999))
            dosya.write("Aktivasyon kodunuz:" + aktivasyon)
        return aktivasyon

    def aktivasyonKontrol(self,aktivasyon):
        aktivasyonKodum = input("Lütfen mailinize gelen aktivasyon kodunu giriniz: ")
        if aktivasyon == aktivasyonKodum:
            return True
        else:
            print("Aktivasyon kodunuz doğrulanamamıştır...")
            return False
        
    def verial(self):
        try:
            with open("C:/Users/Kemalettin/Desktop/kullanıcılar.json","r",encoding="utf-8") as dosya1:
                veriler = json.load(dosya1)
        except FileNotFoundError:
            with open("C:/Users/Kemalettin/Desktop/kullanıcılar.json","w",encoding="utf-8") as dosya1:
                dosya1.write("{}")
            with open("C:/Users/Kemalettin/Desktop/kullanıcılar.json","r",encoding="utf-8") as dosya1:
                veriler = json.load(dosya1)
        return veriler
    
    def veriKaydet(self,kullancıadi,şifre,mail):
        self.veriler = self.verial()
        try:
            self.veriler["Kullanıcılar"].append({"Kullanıcıadı":kullancıadi,"Şifre":şifre,"Mail":mail})
        except KeyError:
            self.veriler["Kullanıcılar"] = list()
            self.veriler["Kullanıcılar"].append({"Kullanıcıadı":kullancıadi,"Şifre":şifre,"Mail":mail})
        
        with open("C:/Users/Kemalettin/Desktop/kullanıcılar.json","w",encoding="utf-8") as dosya1:
            json.dump(self.veriler,dosya1,ensure_ascii=False,indent=4)
            print("Kayıt başarılı bir şekilde oluşturulmuştur....")
        self.menuDon()

    def cikis(self):
        print("Siteden çıkılıyor...")
        time.sleep(0.7)
        self.dongu = False
        exit()

    def menuDon(self):
        while True:
            x = input("Ana menüye dönmek için [5], Çıkmak için lütfen [4]'e basınız.")
            if x == "5":
                print("Ana menüye dönülüyor...")
                time.sleep(0.7)
                self.menu()
                break
            elif x == "4":
                self.cikis()
                break
            else:
                print("Lütfen Geçerli Bir Seçim Yapınız")

Sistem = Site()
while Sistem.dongu:
    Sistem.program()
  