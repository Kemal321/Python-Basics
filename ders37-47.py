# Konumuz built in yani gömülü fonksiyonlar 
print(abs(4)) # mesela abs absolute yani mutlak değer alan fonksiyon gömülü olduğu için direktmen yazarak kullanabiliyoruz. 
              # Normalde bir fonksiyon için kütüphanede vs. bulunur burada gömülü olanlar direktmen dile gömülü olan fonksiyonlar anlamındadır

print(round(22/7,3))  # 2 argümanlı biri yuvarlanacak sayı diğeri ise hassiyettir 3 yaptık mesela hassasiyet 3 virgülden sonra 3 basamak alacak

x= [ 3<4, True, 5<6, 8<9]
print(all(x)) # aldığı değişkenin içindeki değerlerin hepsinin true olup olmadığını boolean olarak dönen bir fonksiyondur

print(any(x)) # itere edilebilir değişkende en az 1 tane bile true değer varsa true dönen bir fonksiyondur all ın tersi durumu gibi düşün

print(ascii("\n")) # genelde kaçış dizilerini direktemn yazdıramadığımız için ascii() fonksiyonunu kullanırız

print(bool(x)) # değişkenimizi durumuna göre boolean değere dönüştüren ve döndüren bir fonksiyondur

print(ord('a'), chr(97)) # bunlarda ascii tablosundaki şekillerini kullanmak istediğimizde mesela ord direktmen onun sayı karşılığını getirirken
                        # chr() ise unicode karşılığını getirir.
a = list()  # list() fonksiyonu bazen boş liste oluşturmak için kullanılır veya farklı tipte verileri listeye çevirmek istediğimizde kullanırız.
print(type(a))

b = "Kemalettin karanın listesi"
z = list(b) 
print(z)  # list() fonksiyonunun ikinci amacı için örnek her bir harfi bir eleman olarak ekleyerek bir liste oluşturdu

v = set() # bu da list() gibi boş küme oluşturmak için kullanılabilir  tamamen list ile aynı mantıkta çalışır ( setlerin kendi özelliklerini unutma)
vv = set(b) 
print(vv)
# tuple() veya dict() fonksiyonlarında da mantık aynı şekilde çalışır float() vs. sonuçta bu direct casting diye geçer java, C, C++ de de vardır 

# c++ deki enum burada bir fonksiyon olarak gömülü şekilde var mesela örnekle gidelim
x = "Kemalettin"
print(enumerate(x)) # direktmen objenin konumunu yazdırır listeleme ile göstermek istersek
print(*enumerate(x)) # bu şekilde listeleyerek de gösterebiliriz 
# genel kullanımı
for i in enumerate(x): # yani aslında itere edilebilir bir nesne döndürür  help() fonksiyonu ile de açıklama görebiliriz
    print(i)
liste = [1,2,3,4,5,6,67,87]
print(max(liste)) # bu ifade adından anlaşılacağı üzere itere edilen nesnenin içindeki en büyük elemanıu döndürür

liste2 = ["A","AB","ABC"]
print(max(liste2, key=len)) # key adındaki 2.anahtar ile string nesleri içinde kullanılabilir burada len uzunluk ölçerdi max len e göre en büyüğü bulur
print(min(liste),sum(liste)) # isminden anlaşılacağı gibi bu şekilde çalışır 
print(*zip(liste,liste2)) # sırasına göre listeleri birleştirir aslında enumeratenin yaptığını iki liste arasında yapar. Normalde itere edilir liste
                          # liste döner
'''
# Mors alfabesi örneği
mors_alfabesi = {
    "A": "•–", "B": "–•••", "C": "–•–•", "D": "–••", "E": "•", 
    "F": "••–•", "G": "––•", "H": "••••", "I": "••", "J": "•–––", 
    "K": "–•–", "L": "•–••", "M": "––", "N": "–•", "O": "–––", 
    "P": "•––•", "Q": "––•–", "R": "•–•", "S": "•••", "T": "–", 
    "U": "••–", "V": "•••–", "W": "•––", "X": "–••–", "Y": "–•––", 
    "Z": "––••",
    "0": "–––––", "1": "•––––", "2": "••–––", "3": "•••––", "4": "••••–",
    "5": "•••••", "6": "–••••", "7": "––•••", "8": "–––••", "9": "––––•",
    ".": "•–•–•–", ",": "––••––", "?": "••––••", "/": "–••–•"
}
morslancek = input("Mors alfabesine çevrilecek metni giriniz lütfen").upper()
morslandı =""
for i in morslancek:
    morslandı += mors_alfabesi[i]
print(morslandı)

'''

'''
# fonksiyon tanımlama kendi fonksiyonlarımızı tanımlicaz
def fonksiyonAdı(parametreler,kaçtaneise):
    uyapılacakİşlemler = parametreler + kaçtaneise
    print("Bu şekilde devam eder ", uyapılacakİşlemler)
fonksiyonAdı(3,5)'''

# Fonksiyonlarda argümanlar

#yukarıda parametre dediğimiz şey diğer adlandırma yöntemi argümandır 
# varsayılan argüman girişi yapabiliriz def toplam(x,y,z=3) mesela burada x y kesin vermemiz lazım z vermezsek otomatik 3 olarak tanımlar geçer
# peki istediğimiz kadar argüman girmek istersek ne yapacağız yıldız kullanacağız def Topla(*x): ... diyerek örnekle görelim
def Topla(*x):
    sayac = 0
    for i in x:
        sayac += i
    return sayac
print(Topla(1,3)) # mesela tek argüman tanımladık ama 2 tane girebildik dönüş olarak da görüldüğü gibi tuple dönüyor yani bunları itere ederek kullanabiliriz

# bunu stringlerle de yapabilirz örneğin
def selamla(*x):
    print(f"Merhaba {x[0] + ' ' + x[1]}, Fonksiyonumuza hoş geldin.") # bu yapıya isteğe bağlı veya keyfi argüman diye adlandırılır args *args diye
selamla("Ahmet","Sonuç")                                              # geçer işte bir de **kwargs var anahtar sözcük argüman şimdi onu görelim

# kwargs yani anahtar sözcük argüman adından da anlaşılacağı üzere sözlük yapısı olarak geçilir yani args tuple idi bu dict olacak
def kalori(**meyve):
    return meyve

print(kalori(Elma= 45, Armut = 50)) # bak burada dict olduğu için direktmen bir key ve value çifti verdim dönüşde bir sözlük olmuş oldu
# kısaca argümanlar bu şekilde şimdi örnek yapalım 

#################### Argümanlar örnek @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def ortalama(*x):
    toplam = 0
    for i in x:
        toplam += i
    return toplam / len(x)
print(ortalama(1,1,1,1,1,1,1,1,1,1,1,1))

def ortalamaKarşılaştır(*args, karşılaştırılacak):
    toplam = 0
    for i in args:
        toplam += i
    sonuc = toplam / len(x)
    if sonuc > karşılaştırılacak:
        print("Girilen değer ortalamadan küçüktür")
    else:
        print("Girilen değer ortalamadan büyüktür")

ortalamaKarşılaştır(1,1,1,1,1,1,karşılaştırılacak=3) # bu şekilde de toplu argümanlar dışında argüman gönderilir


def araba(**kwargs):
    for key, value in kwargs.items():
        if value > 50000:
            print(f"{key} araba biraz pahalı")
        else:
            print(f"{key} araba biraz ucuz")
araba(Audi=70000, BMW = 90000, MERCEDES = 83000, FİAT = 30000)


### lABMDA FONKSİYONU GÜZELDİR ÖNEMLİDİR 
# DAHA kısa işlemler felan varsa lambda ile yapabiliriz toplama örneği
toplam = lambda x,y:x+y
print(toplam(2,2)) # 4 yazdırdı tek satırda bir fonk yani, daha iyi yerler var, listelerde vs. dönecek olursak map() fonk ile
# çok iyi bir kullanım sunar

kareAl = lambda sayi:sayi**2
liste = [1,2,3,4,5] # mesela burada lambdayı tüm listeye döngüye sokmak yerine map() fonk ile hılıca yapcaz
yeniListem = list(map(kareAl, liste)) # yeni listemiz karesi alınmış bir şekilde oluştu
print(yeniListem) # çalışma şekli belli zaten bir fonksiyon ve itere edilecek bir nesne verecez ve bu fonk u bu nesnede 
                  # itere ederek her bir elemana uygulayacak

# global ve local değişkenler c++ ve diğer dillerdeki mantığı farklılığından bahsedeceğim

a = "Merhaba" 
print(a)
def fonksiyon():
    global a
    a = "Global e erişim için global anahtar kelimesini kullanabiliriz ve değiştirebiliriz"
    print(a)
fonksiyon()