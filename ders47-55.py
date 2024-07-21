# nesne tabanlı programlama kısmına geldik c++ daki ile aynı sayılır sntax farklı küçük küçük farklılıklarda var tabi
# aslında kullandığımız değişkenlerde birer sınıf yapısıdır. Nesne tabanlı programlamada sınıflarla çalışacağız.
print(type("Merhaba")) # mesela class str diye döndü

# sınıf yaratma, 
class BoşInsan: # burada isimlendirme kültürü olarak normalden farklı olarak ilk harf büyük harfle başlar
    pass

x = BoşInsan()
print(type(x)) # class str gibi burada da  class Insan olarak çıktı verdi ilk sınıfımızı oluşturduk içini dolduracağız tabi boş insan olmayacağız

class Insan:
    Ad = "Kemalettin"
    Soyadı = "KARA"
    Yaş = 25
    SacRengi = "Kahverengi"

print(Insan.Ad) # burada sadece bir insan oldu ama insan toplu bir tanım olarak olmalı yani her türlü insan olabilir yukarıdaki sınıfımız sadece
                # Kemalettin in sınıfı oldu bencil olmayalım ve bunu genelleyelim başka insanların da tanımlanabilmesi için bu özellikleri 
                # Birer özellik tanımlayıcı hale getirmem lazım ve bunları bir birine bağlayabilmem lazım bunun için ilk tanımlayıcı anlamında
                # def __init__ fonksiyonum ve bunun alacağı parametreler yukarıdakiler ve genel olarak bunları bağlayacak olan parametrem self diye
                # bir şey var bunları kullanacağız 
class Insanlık:
    def __init__(self,Ad,Soyad,Yas,SacRengi):
        self.Ad = Ad
        self.Soyad = Soyad
        self.Yas = Yas
        self.SacRengi = SacRengi

# artık ilk insanı üretebiliriz
IlkInsan = Insanlık("Adem","INSAN","21","Sarı")

print(IlkInsan.Ad) # bu şekilde self ile bağladık init yani initialize ettiğimiz nesneleri adem nesnesi mesela ve onu initialize ettiğimiz attributelerini
                   # özelliklerini çağırabilir kullanabiliriz.

        
### OOP METODLAR YARATMAK 
s = "Kemal"
print(s.index("K")) # Mesela K nin indeksini dönen bu şey bir metoddur ( sınıf içinde çalışan fonksiyon demektir yani)

class Insanlık2:
    def __init__(self,Ad,Soyad,Yas,SacRengi):
        self.Ad = Ad
        self.Soyad = Soyad
        self.Yas = Yas
        self.SacRengi = SacRengi
    
    def bilgiYazdır(self):
        print(f"Merhaba, Benim adım {self.Ad} {self.Yas} yaşındayım") # ilk metodumuzu oluşturduk kontrol edelim

ikinciİnsan = Insanlık2("Adem2", "YALNIZ", 25,"KAHVERENGİ")
ikinciİnsan.bilgiYazdır() # işte bu şekilde çalışıyor

#####KAPSÜLLEME

# c++ daki mantığı ile aynıdır zaten oop mevzusu kendi başına bir konu olarak diğer dillerle aynı çalışır genelde.
# Göstermek istemediğimiz bazı bilgileri vs. kapsülleyerek kullanabiliriz 
class Memur:
    def __init__(self,Ad,Soyad,Maas):
        self.Ad = Ad
        self.Soyad = Soyad
        self.__Maas = Maas 
        self.__ZamOranı = 0.2 ## burada kapsüllemek istediğimiz bilgileri init teki gibi önüne iki alt çizgi ekleriz

memur1 = Memur("Kemalettin","KARA",5000)
# print(memur1.__Maas)  # bu satırı çalıştırdığım zaman kapsüllenen bir bilgiyi yazdırmak istediğim için attribute Error alırım 

# Bu bilgilere ulaşmak için c++ daki gibi getter ve setter yapılarını kullanırız alttaki örnekle bunu görelim 

class Memur2:
    def __init__(self,Ad,Soyad,Maas):
        self.Ad = Ad
        self.Soyad = Soyad
        self.__Maas = Maas 
        self.__ZamOranı = 0.2 ## burada kapsüllemek istediğimiz bilgileri init teki gibi önüne iki alt çizgi ekleriz
    def getMaas(self):
        return self.__Maas  # artık bu yapı ile Maaş bilgisini alabiliriz fonksiyonun get ve set ile oluşması lazımdır unutma
    def setMaas(self,yeniMaas):
        self.__Maas = yeniMaas

    
memur2 = Memur2("Ahmet","YILMAZ",3000)
print(memur2.getMaas()) # bu şekilde kapsüllenmiş bilgiye ulaştık maaş bilgisini ise değiştirmek için set yani setter yapısı ile dğeiştirebiliriz sadece
memur2.setMaas(4000)
print(memur2.getMaas()) # sonuç 4000 olarak gelmiş oldu 


# MİRASLAMA 

# Kısaca oluşturduğumuz sınıfa başka bir sınıfın özelliklerini almak olarak düşünün babamızın genlerini taşımamız gibi o yüzden kalıtım olarak 
# da adlandırılır 
'''class Insan():                                          # Bu ana sınıfımız olsun bir de öğrenci sınıfı oluşturmak istedik diyelim ki 
    def __init__(self,Ad,Soyad,Yas,SacRengi,Boy,Kilo):   # Oluşturacağımız öğrenci sınıfında olacak kişilerde aslında bir insandır o yüzden 
        self.Ad = Ad                                     # Ad soyad boy kilo vs. bilgileri orada da olacak o yüzden bunları kalıtmak iş yükümüzü azaltır
        self.Soyad = Soyad
        self.Yas = Yas
        self.SacRengi = SacRengi
        self.Boy = Boy
        self.Kilo = Kilo
class Ogrenci(Insan): # Kullanım şekli bu şekilde kalıtılacak class ı yeni oluşturulan sınıfın içine yazarız
    def __init__(self, Ad, Soyad, Yas, SacRengi, Boy, Kilo, sınıf,Bolum):  # init yazıp tab a basınca kendisi otomatik doldurdu zaten super() 
        super().__init__(Ad, Soyad, Yas, SacRengi, Boy, Kilo)  # kısmındaki özellikler Miras aldığımız yerden geliyor yeni özellikleri üste ekliyoruz
        self.sınıf = sınıf
        self.Bolum = Bolum '''

# Bundan sonra kullanımı aynı normal sınıf nesnesi tanımlama ve kullanma şeklinde devam eder.
        
### ÖRNEK - ATM UYGULAMASI
# Burayı sadece izledik uygulamasını yapacağız tabi - yazbel den bitirelim diye düşünüyoruz.

##############################MODÜLLER ###################
# pypi.org sitesinden yararlanılabilir bir çok modül release ve projeler orada paylaşılşır onun dışında daha önce gördümüz modül ve kütüphaneler 
# sürekli kullanılabilecek end to end fonksiyon, uygulama vs. kodlarının taşınabilir bir şekilde paket halinde tutulduğu yapılardır
# Bunları kullanırken öncelikle import dediğimiz ekleme işlemini yapmamız lazım mesela import kütüphaneadı
# Burada ekleme yaparken bir kütüphanenin içindenm sadece bir modül de eklemek istiyor olabiliriz 
# from kütüphane import buModül as benimİsterdiğimTakmaİsim ile syntax bu şekilde çalışır 
# help(modülİsmi) veya help(modülİsmi.fonksiyon) şeklinde help yapısını kullanarak bunlar hakkında bilgi de alabiliriz. 

########## MATH KÜTÜPHANESİ #############
import math 
# print(help(math)) # Buradan kısaca ne olduğunu hangi fonksiyonlar olduğunu gösterir 
# Mesela burada bazı fonksiyonları görelim 
print(math.pow(2,3)) # üs alma işlemi gerçekleştirir
print(math.floor(2.7)) # aşağı yuvarlama işlemi yapar 
print(math.sqrt(25)) # karekök alma işlemi gerçekleştirir
print(math.factorial(2)) # faktöryel alma işlemi gerçekleştirir diğer notları istihzadan okuduk ve hackerrank de tamamladık bir kaç örnek daha görelim
print(math.ceil(2.3)) # yukarı yönlü yuvarlar.
# Burada mesela hep math.fonksiyonadı şeklinde kullandık fakat bir kütüphanede bunu kullanmak istemiyorsak from kütüphaneadı import* şeklinde import
# edersek istediğimiz gibi kullanabiliriz














        