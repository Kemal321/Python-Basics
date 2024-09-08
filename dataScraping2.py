'''
Daha geniş bir örnek yaptık. İş yatırım sitesinden bazı hisselerin bazı finansal bilgilerini alacağız. 


'''
import requests
from bs4 import BeautifulSoup
import re
import time 

class Hisse():
    def __init__(self):
        self.dongu = True

    def program(self):
        secim = self.menu()

        if secim == "1":
            print("Güncel Fiyatlar Alınıyor...\n")
            time.sleep(1.3)
            self.guncelFiyat()
        if secim == "2":
            print("Künye Bilgileri Alınıyor...\n")
            time.sleep(1.3)
            self.kunye()
        if secim == "3":
            print("Cari Değerler Alınıyor...\n")
            time.sleep(1.3)
            self.cariDeger()
        if secim == "4":
            print("Getiri Değerleri Alınıyor...\n")
            time.sleep(1.3)
            self.getiri()
        if secim == "5":
            print("Endeks Ağırlıkları Alınıyor...\n")
            time.sleep(1.3)
            self.dahilEndeks()
        if secim == "6":
            print("Ortaklık yapısı Alınıyor...")
            time.sleep(1.2)
            self.ortaklikYapisi()
        if secim == "7":
            print("Otomasyondan Çıkılıyor...\nTeşekkür ederiz...")
            time.sleep(1.3)
            self.cikis()

    def menu(self):
        def kontrol(secim):
            if re.search("[^1-7]",secim):
                raise Exception("Lütfen 1 ile 7 arasında bir seçim yapınız")
            if len(secim) != 1:
                raise Exception("Lütfen 1-7 arasında bir seçim giriniz.")
        while True:
            try:
                secim = input("Merhaba Hisse otomasyon sistemine hoş geldiniz.\n\nLütfen yapmak istediğiniz işlemis seçiniz...\n\n[1]-Güncel Değerler\n[2]-Şirket Künyesi\n[3]-Cari Değerler\n[4]-Getiri Değerleri\n[5]-Dahili Endeksler\n[6]-Ortaklık Yapısı\n[7]-Çıkış\n-->")
                kontrol(secim)
            except Exception as hata:
                print(hata)
            else:
                return secim
        
    def guncelFiyat(self):
        while True:
            try:
                SIRKET = input("Aramak istediğiniz hisse kodunu giriniz: ")

                url ="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/default.aspx"

                parser = BeautifulSoup(requests.get(url).content,"html.parser")
                fiyat = parser.find("a",{"href":"/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(SIRKET.upper())}).parent.parent.find_all("td")
                FIYAT = fiyat[1].string
                YUZDEDEGISIM = fiyat[2].span.string
                TLDEGISIM = fiyat[3].string
                TLHACIM = fiyat[4].string
                ADETHACIM = fiyat[5].string
                print(f"Hisse Fiyatı: {FIYAT}\nYüzde bazlı değişim: %{YUZDEDEGISIM.strip()}\nTL bazlı değişim: {TLDEGISIM} ₺\nTL bazlı hacim: {TLHACIM} ₺\nAdet bazlı hacim: {ADETHACIM}")
            except AttributeError:
                print("Hatalı bir giriş yaptınız...")
                time.sleep(0.4)
            time.sleep(0.3)
            self.menuDon()

    def kunye(self):
        while True:
            try:
                SIRKET = input("Lütfen aramak istediğiniz şirket kodunu giriniz: ").upper()   
                url = f"https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={SIRKET}"
                parser = BeautifulSoup(requests.get(url).content,"html.parser")

                KUNYE = parser.find("div", {"id":"ctl00_ctl58_g_6618a196_7edb_4964_a018_a88cc6875488"}).find_all("tr")
                for i in KUNYE:
                    bilgi1 = i.td.string
                    bilgi2 = i.th.string
                    print(f"{bilgi2} = {bilgi1}")
                break
            except AttributeError:
                print("Hatalı bir giriş yaptınız...")
                time.sleep(0.4)
        time.sleep(0.3)
        self.menuDon()   

    def cariDeger(self):
        while True:
            try:
                SIRKET = input("Lütfen aramak istediğiniz şirket kodunu giriniz: ").upper()   
                url = f"https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={SIRKET}"
                parser = BeautifulSoup(requests.get(url).content,"html.parser")

                CARI = parser.find("div", {"id":"ctl00_ctl58_g_76ae4504_9743_4791_98df_dce2ca95cc0d"}).find_all("tr")
                for i in CARI:
                    bilgi1 = i.td.string
                    bilgi2 = i.th.string
                    print(f"{bilgi2}: {bilgi1}")
                break
            except AttributeError:
                print("Hatalı bir giriş yaptınız...")
                time.sleep(0.4)
        time.sleep(0.3)
        self.menuDon() 
    
    def getiri(self):
        while True:
            try:
                SIRKET = input("Lütfen aramak istediğiniz şirket kodunu giriniz: ").upper()   
                url = f"https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={SIRKET}"
                parser = BeautifulSoup(requests.get(url).content,"html.parser")

                GETIRI = parser.find("div", {"id":"ctl00_ctl58_g_aa8fd74f_f3b0_41b2_9767_ea6f3a837982"}).find("table").find("tbody").find_all("tr")
                for i in GETIRI:
                    bilgi = i.find_all("td")
                    print(f"Birim:{bilgi[0].string} Günlük(%): {bilgi[1].string} Haftalık(%): {bilgi[2].string} Aylık(%): {bilgi[3].string} Yıl içi(%): {bilgi[4].string}")
                break
            except AttributeError:
                print("Hatalı bir giriş yaptınız...")
                time.sleep(0.4)
        time.sleep(0.3)
        self.menuDon() 
    
    def dahilEndeks(self):
        while True:
            try:
                SIRKET = input("Lütfen aramak istediğiniz şirket kodunu giriniz: ").upper()   
                url = f"https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={SIRKET}"
                parser = BeautifulSoup(requests.get(url).content,"html.parser")

                ENDEKSLER = parser.find("div", {"id":"ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"}).find("table").find("thead").find("tr").find_all("th")
                ENDEKSDAHILLIK = GETIRI = parser.find("div", {"id":"ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"}).find("table").find("tbody").find("tr").find_all("td")
                print(f"{ENDEKSLER[0].string}: {ENDEKSDAHILLIK[0].string}\n{ENDEKSLER[1].string}: {ENDEKSDAHILLIK[1].string}\n{ENDEKSLER[2].string}: {ENDEKSDAHILLIK[2].string}")
                break
            except AttributeError:
                print("Hatalı bir giriş yaptınız...")
                time.sleep(0.4)
        time.sleep(0.3)
        self.menuDon() 

    '''
    Burada var olan kodların çalışmamasının nedeni iş bankası sitesinin dinamik html olarak kodları eklemesidir.
    Bunu çözmenin en efektif yolları selenium kütüphanesinin kullanılması veya API request yaparak alınan bilgileri json olarak
    saklanması ile en mantıklı ve efektif çözümler yapılabilir veya javascript kullanılarak çözülebilir. Fakat benim alanımda bu 
    konular şuanlık kapsanmadığı içinyapmayacağım. Geriye kalan proje detaylı olarak kodlanmış ve çalışmaktadır. 
    def ortaklikYapisi(self):
        while True:
            try:
                SIRKET = input("Lütfen aramak istediğiniz şirket kodunu giriniz: ").upper()   
                url = f"https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={SIRKET}"
                parser = BeautifulSoup(requests.get(url).content,"html.parser")

                UNVANPAY = "ORTAKLIK YAPISI TABLOSU\n--------------------------------------------------------------------"
                PAYORAN = parser.find("table", {"id":"partnerShipTable"})
                for i in PAYORAN:
                    print(f"{i.td.string}: {i.td.find_next_sibling("td").string}")
                break
            except AttributeError:
                print("Hatalı bir giriş yaptınız...")
                time.sleep(0.4)
        time.sleep(0.3)
        self.menuDon() '''
        
    def cikis(self):
        self.dongu = False
        exit()

    def menuDon(self):
        while True:
            x = input("Çıkmak için 6'ya, Ana menüye dönmek için Lütfen 8'e basınız...: ")
            if x == "6":
                self.cikis()
            if x == "8":
                print("Ana menüye dönülüyor...")
                time.sleep(1.3)
                self.program()
                break
            else:
                print("Lütfen geçerli bir seçim yapınız....")
    
Sistem = Hisse()
while Sistem.dongu:
    Sistem.program()