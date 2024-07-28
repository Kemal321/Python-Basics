########################## Decorator ##############################
'''
Bir fonksiyona veya bir den fazla fonksiyona dışarıdan ek özellik eklemeye yarayan yapılardır. 
Bunun için bazı şeyleri bilmek gerek ilk olarak onlardan bahsederek ilerleyeceğiz sonrasında decoratorları ( bezeyici ) tam olarak göreceğiz
'''

# ilk olarak bir fonksiyonu tanımladıktan sonra parantezleri kullanmadan bir değişkene atadığımızda o değişkeni fonksiyonmuş gibi kullanabiliriz.

# örnek 
def topla(x,y):
    sonuc = x + y
    print(sonuc)

ornek = topla  # Dikkat edin parantezleri kullanmıyoruz, kullanırsak direktmen fonksiyonu çağırmış oluruz.

ornek(2,1) # böylece ornek ismini sanki topla fonksiyonu gibi kullanabiliyoruz. 


def fonksiyon1():
    print("Merhaba")

    def fonksiyon2():
        return "Nasılsın"
    
    print(fonksiyon2)

fonksiyon1() # bak mesela burada merhaba \n nasılsın diye yazdıracak burada return ifadesi fonksiyonun ne olarak döndürüleceğidir.
            # yukarıda fonksiyon1 e fonksiyon 2 yi de ekleyerek ek bir işlev sağlamış olduk. 
            # ama mesela bunun gibi 10 farklı modülü olsaydı kodun bu sefer uzayacaktı ve bu taşınabilir bir şey olmaktan çıkacak ve maliyetli 
            # olmaya başlayacak işte tam bu noktada Decoratorlar ( bezeyici ) ortaya çıkıyor. Nedir bu eleman 

'''
Decorator da yukarıda yaptığımızdan farklı bir şey değil zaten. 
yani fonksiyon2 yi decorator bir fonksiyon olarak tanımlarız ve diğer fonksiyonlara eklerken onları fonksiyon2 ile bezer iken :))
Kullanıyoruz işte bu noktada yukarıda ki maliyet vs. sorunlarını bir kısmını halletmiş oluruz tek bir ifade ile bir çok yerde kullanarak modülerlik
kazanmış ve karmaşıklığı azaltmış oluruz. 
'''
'''
# decorator yapısı kurma basitçe görelim 

def fonksiyon1(fonksiyon):
    def wrapper():
        print("Decoratorlarda genelde wrapper olarak adlandırılı bu fonksiyon")
        fonksiyon() # burada ana fonktaki fonksiyon ismi aynı classlardaki self gibi olacak yani bezeyeceğimiz fonksiyon burada olacak
        print("Artık bezenecek fonksiyon bu iki print arasında kalacak ve printlerde çalışarak onu bezeyecek")
    return wrapper
# bunu yaparken tabiki bir şey kullanacağız decoratorun adı neydi fonksiyon1 istediğimizi kullanıyoz orda zati. bunu 
# bezeyeceğimiz fonksiyonun hemen öncesine @fonksiyon1 diyerek eklicez artık decorator fonk. umuzun adı neyse onu kullancaz yani

@fonksiyon1 # bezeme işlemi        
def selamla():
    print("Selam bezenecek fonksiyon benim. ")

# bezenmiş fonksiyonun davranışını görebilirsin bunun sonucu ile. 
selamla()


Burada parametreli halide var tabiki unutmamak lazım decorator olan fonksiyonumuzun argüman sayısı ile 
bezenecek olan yani decore edilecek olan fonksiyonumuzun argüman sayısı vs. de aynı olmalıdır yoksa hata döner
'''
'''

def deco(bezeyici):
    def wrapper(x,y):
        print("İşleminizin sonucu..: ")
        bezeyici(x,y)
    return wrapper

@deco
def toplama(x,y): # bakın mesela x ve y olmalı yoksa hata verir
    sonuc = x +y
    print(sonuc)

toplama(3,1) #gördüğünüz gibi bu şekilde bezendi

# daha uygun bir örnek görelim daha iyi anlamak adına
import time

def zamanolc(bezenecek):
    def wrapper(*args,**kwargs):
        basla = time.time()
        time.sleep(2)
        bezenecek(*args,**kwargs)
        bitis= time.time()
        gecenSure= bitis-basla
        print("Fonksiyon {} kadar sürede işlevini gerçekleştirdi.".format(gecenSure))
    return wrapper


@zamanolc
def topla(x,y):
    sonuc = x + y
    print(sonuc)
@zamanolc
def çarp(x,y):
    sonuc = x*y
    print(sonuc)
@zamanolc
def bol(x,y):
    sonuc = x/y
    print(sonuc)


topla(1,0)
çarp(1,1)
bol(2,2)
'''
'''
Mesela artık zaman ölçmek için ekstra bir şey yapmamıza gerek yok sadece @zamanolc diyerek fonksiyon ne kadar zamanda işlevini yerine
getiriyor bunu bulabiliriz. İşte decoratorların gücü burada ortaya çıkıyor. Aşırı güzel modüler sistemleri tasarlarken sadece 1 kere hazırladığımız
bir fonksiyonla bu işlevselliği her yere götürebiliyoruz

'''

###########################ITERATORLAR#################################

''' 
Adından belli iteratorlar yani yineleyiciler bir nevi geziciler daha önce c++ de de görmüştük orada tabi herşey daha derindi burada biraz daha normal
anlatacağız. İteratorlar öncelikle bir döngü oluşturmak için arka planda çalışan sistemlerdir mesela for döngüsünün çalışması için
bu iterator nesneleri ve mantalitesi çalışır aslında. Hatalarda gördüğümüz object is not iterable gibisinden hatalar görürürüz mesela stringler 
iterable nesnelerdir. Harf harf gezeriz bunun gibi lafı uzatmadan örneklerle bu durumu açıklayalım.
'''

liste = [1,2,3,4,5]

# normal for döngüsü
for i in liste:
    print(i) # bak eleman eleman gezecek döngü oluşcak ve ekrana basacak

iterci = iter(liste) # burada ise iter() ile bir fonksiyon oluşturdum. 

print(next(iterci)) # burada next fonksiyonu ile bu iterator fonksiyonunun ürettiği nesneye bakıyorum 
print(next(iterci))
# art arda print(next(iterci)) yazarak bir döngü oluştururuz 
# ama bu döngü işlemince next() fonksiyonuna mesela yukarıda 5 elemanlı itere edilebilir liste türünde bir değişken verdik 
# 6 kere next çalışsaydık StopIteration hatası alırdık for döngüsü de bunu aşağıdaki gibi basit bir yapı ile çözer aslında
#burada da iterator fonksiyonu kullanarak for döngüsünü görelim mesela

while True:
    try:
        tara =  next(iterci)
        print(tara)
    except StopIteration:
        break

# gördüğünüz gibi bu durum bu kadar basit bir şekilde çalışır ilerleyen örneklerle konuyu daha iyi kavramaya çalışayım.

# bir iterasyon yapısı yapalım 
class SayılarIteratoru:
    def __init__(self,basla,bitis):
        self.basla = basla
        self.bitis = bitis

    def __iter__(self):
        return self

    def __next__(self):
        if self.basla < self.bitis:
            x = self.basla
            self.basla += 1
            return x
        else:
            raise StopIteration
            
print(SayılarIteratoru) # buradan nasıl bir şey ürettiğimizi görelim evet  <class '__main__.SayılarIteratoru'> çıktısı verdi
liste = SayılarIteratoru(1,10) # mesela burada bir basla ve bitis adlı 2 parametreyi belirledim ve burada bir iterasyon yapan sınıf tanımladım kullandım
for i in liste:
    print(i)
    
###########################GENERATOR ( ÜRETEÇLER )#################################

'''
Iterator ile aynı mantalitede çalışan daha sade bir yapı ile yazmamızı daha da önemlisi bellekte sürekli yer kaplamamasını istediğimiz yapılarda
bunu kullanırız.
'''
# mesela durumu tekrar gözetelim 
liste = [1,2,3]

itercim = iter(liste)

print(itercim) # <list_iterator object at 0x00000259E904B9D0> dönütü ile aslında bellekte bir yer ayrıldığını görüyoruz işte generator bu noktada 
# bize avantaj sağlayacak

# mesela klasik bir iterasyon örneğini görelim ve bunu generator a çevirelim. mesela 1 den başlayarak tek sayıları yazdıran bir sistem

def tek(sayı):
    liste = []
    for i in range(0,sayı):
        liste.append(i*2+1)
    return liste

print(tek(100))

# iteratorlu olanı kısaca bu şekilde. Şimdi de generator yapısına bakalım 

def tek(sayı):
    # burada artık hafızada tutulmicak dedik o zaman listeye gerek kalmicak demektir :d
    for i in range(0,sayı):
        # artık burada da liste olmadığına göre ekleme yapabileceğim bir şey yok işte burada yield dediğimiz bir şey devreye giriyor 
        yield (i*2-1) # return gibi düşünebiliriz yield den sonra istediğimiz işlemi yerleştirdik. 
    
for i in tek(100):
    print(i)

# ama dikkat etmek gerek ki burada fazladan bir for döngüsü daha gerçekleştirdik e tabi her hamlenin getirisi kadar götürüsü de olacak işte 
# bu noktada mühendis dediğimiz mucizevi biyolojik varlık verdiği kararlar ile en optimal sistemi kuracak. :)) 