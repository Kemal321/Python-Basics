from datetime import*  # bu kullanımı daha önce içe aktarmayıu öğrendiğimizde görmüştük herşeyi alıyor 
import time # genelde gecikme istenen yerlerde bu kütüphanede var olan parçalar kullanılır mesela hemen örnek verelim
'''while True:
    zaman = time.strftime("%H:%M:%S")
    print(zaman)
    time.sleep(3)''' # yani saati dakikayı ve saniyeyi yazacak ve sleep(3) 3 saniye uyuyacak böyle on nümera

zmana = datetime.now() # burada da datetime ı kullanmamın nedeni normalde * ile aldık herşey aldığımız içni isme gerek yok 
                       # ama burada datetime ın içinde datetime adında bir sınıf daha var. O yüzden bunu kullanıyoruz. 
                       # kafan karışmasın yani
dogumGunu = datetime(1999,4,28)
bugun = datetime.today() 
fark = bugun - dogumGunu # zamanları bir birinden çıkartabiliyoruz burada yaptığımız gibi ama sadece gün saniye dakika ve 
                         # mikrosaniye bakımından farkı öğretir
# ek olarak timedelta() fonksiyon olarak da direktmen kullanılır mesela 
bugun = datetime.today()
fark = timedelta(days = 365) # burada 365 günlük bir zaman farkı diyorum 
print(fark, bugun,sep="\n") # buradan kontrol edebilirsin yani farkın kendisi direktmen bir zaman küpü olarak 365 gündür

# bu oluşturulan ayrık zamanı başka zamanlara ekleyerek iler veya geri tarihi bulabiliriz mesela 

gelecekFatura = bugun + fark
print("Gelecek faturanız: ",gelecekFatura," tarihinde olacaktır.")

######################### RANDOM KÜTÜPHANESİ #############################
import random

x = random.random()  # rastgele float değer döner. Rassal sayı üretmek için kullanılır yani c++ de daha detaylısını görmüştük mersenne twister gibi.
print(x)   # 0 ile 1 arasında rastgele sayı üretir.

xx = random.uniform(1,100) # burada ise istediğimiz aralıkta rastgele sayılar üretir 
# illa ki float değer üretilmez örneğin 
xxx = random.randint(1,100) # 2 zorunlu parametre alır bunlar hangi aralıktan sayı üretceğimizi belirtir
print(xxx) #burada rastgele int olan bir sayı üretecek mesela 

# bir diğer faideli fonksiyonumuz random.choice(iterator) 

liste = ['ali', 'veli', 'ahmet', 'mehmet', 'celal', 'selin', 'nihat'] 
# böyle bir listeden choice yardımı ile rastgele seçim yapabiliriz
print(random.choice(liste))


# bir diğer fonksiyonumuz sample() bu da verdiğimiz yığın tarzı verilerin arasında örneklemler seçer örneğin 
liste2 = range(0,100) 
print(random.sample(liste2,10)) # mesela 1.parametre hangi koleksiyondan , 2.parametre kaç adet örneklem olacağı 

# random.shuffle(liste2) # bu da karıştırır shuffle eder yani koleksiyonda var olan verilerin karar

# bir de randint için randrnage() fonksiyonu da vardır küçük farklılıkları var ona bakarsın netten basit zati


import os # istihzadan bak çok derin değil zaten 

# os.startfile(os.curdir) # çalıştırınca mevcut dizini açıyor o yüzden yorum satırına çevirdim 

print(os.getcwd())

###########################KENDİ MODÜLÜNÜZÜ YAZMAK ################################
# c++ gibi ifndef yapısı vs. oluşturmana gerek yok pragma once veya, burada fonksyionları vs. modülerleştirdikten sonra bir py dosyasına koyarsak 
# ve import ettik mi bitti 

################ HATA YAPILARI #################
#x = int(input("Lütfen bir sayı giriniz: ")) # kullanıcıdan kaynaklı hataları programı durdurmadan sürekli çalışabilecek bir program yapmamız lazım 
                                            # bu yüzden hata yapıları ile bu hataları yakalayabilir ve handle edebiliriz.

################### TRY -EXCEPT YAPISI ##########################

'''try: 
    x = int(input("Lütfen bir sayı giriniz: "))
    y = int(input("Lütfen bir sayı giriniz: ")) 
    print(x/y)
except:  # burada bu şekilde bırakırsak tüm hatalarda alt taraftaki block çalıştırılır. 
    print("Yolunda gitmeyen bir şeyler var....")


try: 
    x2= int(input("Lütfen bir sayı giriniz: "))
    y2 = int(input("Lütfen bir sayı giriniz: ")) 
    print(x2/y2)
except ZeroDivisionError:  # Ya da bu şekilde bir tane hataya odaklanabilir ve dallandırarak gidebiliriz.
    print("Yolunda gitmeyen bir şeyler var....")
except ValueError:
    print("Değer girdilerinde bir hata lütfen istenilen türe dikkat ediniz")


try: 
    x = int(input("Lütfen bir sayı giriniz: "))
    y = int(input("Lütfen bir sayı giriniz: ")) 
    print(x/y)
except (ZeroDivisionError, ValueError):  # Veya bu şekilde belirli hata gruplarına karşı belirli çözüm yöntemleri yakalama yöntemleri de uygulayabiliriz
    print("Yolunda gitmeyen bir şeyler var....")


while True:
    try:  # aynı zamanda try grubu else ile de çalışır excepten sonra else koyarak mesela hata yok else çalışır döngü ile bir şeyler alarak 
        # işler yapabiliriz mesela stdin tarafını boşaltabiliriz vs. vs.
        x = int(input("Lütfen bir sayı giriniz: "))
        y = int(input("Lütfen bir sayı giriniz: ")) 
        print(x/y)
    except:  # burada bu şekilde bırakırsak tüm hatalarda alt taraftaki block çalıştırılır. 
        print("Yolunda gitmeyen bir şeyler var....")
    else:
        break

# bunlara ek olarak kullanıcının da görmesini istersek exception yapısını kullanabiliriz
    
try: 
    x = int(input("Lütfen bir sayı giriniz: "))
    y = int(input("Lütfen bir sayı giriniz: ")) 
    print(x/y)
except Exception as hata:  # burada bu şekilde bırakırsak tüm hatalarda alt taraftaki block çalıştırılır. 
    print("Yolunda gitmeyen bir şeyler var....",hata)

'''

#################### RAİSE YAPISI #################
# Burada hata olmayıp bizim istediğimiz şeylerin dışında girdi vs. durumları olursa bunları yakalamak içni raise yapısını kullanıyoruz
# mesela kullanıcıdan 0 dışında bir sayı girmesini istediğimiz halde adam inatla 0 giriyorsa bu hata değildir ama bizim semantic yapımızda bu hata
# olarak algılanır işte bu durumların tespitinde raise yapısı kullanılır 
    
#örnekle görelim  
'''def kontrol(x):
    if len(x)<5:
        raise Exception("Şifreniz en az 5 karakterden oluşmalıdır.\nŞifrenizi tekrar deneyiniz.")
    else:
        print("Şifreniz başarılı bir şekilde oluşturulmuştur.")

try: 
    x = input("Giriş için bir şifre oluşturunuz lütfen")
    kontrol(x)
except Exception as hata:
    print(hata)'''
# mesela bu örnekte oluşturmak istediğimiz şifreyi input ile aldık ve şifre 5 karakterden küçük bunu hemen kontrol() adlı fonk. oluşturarak
# kontrol ettik ve 5 ten küçük olduğu hale raise yapısını kullandık kullanımı basit bu şekildedir .     

import re

x = "Kemalettin KARA başaracak"

y = re.findall("başaracak",x) # bu fonksiyon verilen parametreyi 2.parametrede belirtilen konumda arayacak bulursa y değişkenine liste olarak 
print(y)                      # atacayacak bulamaz ise y yi boş bırakacak


z = re.split(" ",x) # buradaki split fonksiyonu stringlerdeki split ile aynı mantıkta çalışır
print(z)

z = re.sub(" ","*",x) # sub fonksiyonun görevi x değişkeninde ilk parametreleri bul ve 2.parametre ile değiştir demek örnekteki gibi
print(z)

y = re.search("başaracak",x) # 2.parametrede girilen değişken üzerinde 1.parametreyi arar ve bir re.Match objesi döndürür 
print(y)                     # bu obje bize span ve match adında iki bilgi ile döner span parametresi aranılan şeyin kaçıncı parametreden başlayıp
                             # kaçıncı parametrede bittiğini gösterir. match ise yani kendisi bizim aradığımız değerin ne olduğunu gösterir
print(y.span(), ) # burada nesnenin kendi attributesini kullanabiliriz span olanı yani bu bilgiyi de ayrı alabiliriz, sadece span ı unutma
                # tuple olarak döner bazı fonksyionları vardır start başlangıç yeri end bitiş yeri gibi y.start() y.end() gibi 
print(y.string)  # bu bir attribute değildir o yüzden paranteze gerek yoktur. Burada aramak istediğimiz şeyi nerede aradığımızı gösterir. 

y = re.findall("[a-z]",x) #burada a-z arasındaki harfleri x te ara diyerek kullanabiliriz
print(y)
y = re.findall("[A-Z]",x) # burada farklı farklı şeyleri bulabiliriz bunları dökümantasyondan bakarak kullana kullana alışırız
print(y) 
# burada şapka kullanımı not yani değil anlamı taşır [^a-z] burada a-z arasında olmayan şeyleri bul anlamında kullanılır. 
y = re.findall("[^a-f]",x)
print(y) # çıktıya bakarsanız a b c d e f harflerinden hiç biri yok büyükleri olabilir case sensitive bir dil unutmayın 

# Türkçe karakterleri manuel eklemek gerekiyor y=re.findall("[A-ZÇŞĞİÜÖ]", x ) bu şekilde bir kullanımı oluyor 

y = re.findall("^M",x) # bunun anlamı x M harfi ile mi başlıyor diye sorgulamaktır eğer başlıyorsa y değişkeni ['M'] bu şekilde olur 
print(y)               # başlamıyorsa boş liste döner aynı bu örnekte olduğu gibi
y = re.findall("k$",x) # dolar işareti ise yapının son karakterini kontrol eder
print(y)               # x değişkeninin son harfi küçük k olduğu için y küçük k harfini içeren bir liste olarak döner ['k']

y = re.findall("...",x) # 3 er karaktere bölerek liste şeklinde dönüş sağlar, boşlukta karakterdir
print(y)

y = re.findall("\s", x) # kaç boşluk olduğunu döner zaten \s space manasında boşluk karakteri yani
print(y) # mesela bunu bir yapıda 3 boşluk dışında kullanmasını istemiyorsak bunu kullanıl len(y) diyip kontrol edebiliriz 


################### Şifre oluşturma uygulaması ( RE modülü ve hata yakalama yapısı ile alakalı) ####################

'''dogumTarihi ="1999"
karakter =["\?","\*","\!","\%"] #bunu tanımlamamın nedeni özel karakterleri kullanmasını isteyeceğimiz için bunu oluşturuyoruz 
# Ters taksim ile tanımlamamızın nedeni re modülünde özel karakter olarak da kullanıldıkları için çakışmalarını istemiyoruz.

def sifreKontrol(sifre):
    if len(sifre) < 8:
        raise Exception("Şifreniz en az 8 karakterden oluşmalıdır.")
    elif not re.search("[a-z]",sifre): # Burada şunu demek istiyoruz a ile z arasındaki harflerden 1 tane bile yoksa hata sayacağımız için bunu koyduk
        raise Exception("Şifreniz en az 1 küçük harf içermelidir.")
    elif not re.search("[A-Z]",sifre):
        raise Exception("Şifreniz en az 1 büyük harf içermelidir.")
    elif not re.search("[0-9]",sifre):
        raise Exception("Şifreniz en az 1 rakam içermelidir.")
    elif not re.search(str(karakter),sifre):
        raise Exception("Şifreniz en az 1 özel karakter içermelidir ( ? ! * %).")
    elif sifre.startswith(dogumTarihi):
        raise Exception("Şifreniz doğum tarihiniz ile başlayamaz.")
    elif sifre.endswith(dogumTarihi):
        raise Exception("Şifreniz doğum tarihiniz ile bitemez.")      
    else:
        print("Şifreniz başarılı bir şekilde oluşturulmuştur.")

while True:
    try:
        sifre = input("Lütfen oluşturmak istediğiniz şifreyi giriniz: ")
        sifreKontrol(sifre)
    except Exception as hata:
        print(hata)
    else:
        break   

'''
################################# DOSYA İŞLEMLERİ ##############################################

# Bu konu da python ile her hangi bir dosyaya erişmek o dosyadan veriler çekmek onunla işlemler yapmak için var olan bir konudur 
# İlk olarak python üzerinden bir dosyaya erişebilmek için ilk olarak open() adında bir fonksyion kullanmamız gerekir. 
# 4 temel dosya işlemi vardır bunlar w modu ( write - yazma ) a modu ( append - ekleme ), r modu ( read - okuma ), x modu ( oluşturma modu )

dosya = open("Merhaba.txt","w") # Burada yapı open("dosyaAdı", "DosyaModu" )
#w modu biraz da tehlikelidir çünkü oluşturmak istediğimiz dosya zaten mevcutsa onu siler ve sıfırdan oluşturur. Kaybolmasını istemediğimiz 
# bir şeyler varsa tehlikeli olmuş olur. Değişken tanımlamamızın nedeni ise dosya. diyerek yapacağımız işlemleri bu değişken üzerinden yapacağız.
# Dosya açıldıktan sonra kapatılmazsa arka planda her zaman açık kalır. "C:/Desktop.../merhaba.txt" şeklinde istediğimiz dizinde de oluşturabiliriz.

dosya.write("Merhaba bu write modu her çalıştığında dosyanın içindekileri de siler ona göre. Her çalıştığında içinde sadece 1 kere görürsün")
dosya.close()  # bu şekilde de kapatmak gerekir 

dosya2 = open("Merhaba2.txt","a")
dosya2.write("Kardeşim burada bu eleman her seferind ekleme yapar yani içindekileri silmez. W modu yerine bunu kullanabiliriz.")
dosya2.close()

# x modu ise w modu ile aynı ama eğer oluşturulmak istenilen dosya zaten var ise hata döndürür. 
# dosya2 = open("Merhaba.txt","x") # bu satırı çalıştırdığımızdı File already exist diyerek hata döner. 
dosya3 = open("Merhaba3.txt","r") # r modu okuma modudur bazı ek fonksiyonları da vardır onları da biraz biraz göreceğiz 


print(dosya3.read()) # bu dosyadaki verileri okuyup ekrana yazdırabiliriz. 
for i in dosya3: # burada da for döngüsü kullanarak dosyanon içindekileri tek tek de alabilriiz satır satır işlem yapar. 
    print(i,end=" ")

dosya3.close()

dosya3 = open("Merhaba3.txt","r")

'''print(dosya3.readline()) # bu fonksiyon ise satır satır okuma işlemi yapar. 
print(dosya3.readlines()) # bu fonksiyon ise tüm satırları liste olarak döner bir değişkene atayarak liste tipinde saklayabiliriz. 
'''
ilkKaçHarf = 3
print(dosya3.read(ilkKaçHarf)) # burada ise read ile aynı zamanda belirtilen parametre ile ( int ) ilk x tane harfi döner. 
dosya.close()

with open("Merhaba.txt","r") as Dosya:  # Merhaba txt yi read modunda Dosya adı ile aç demek bu ve bir blok olarak çalışır. 
    print(Dosya.read())
# Burada mevzu close() yapısını unutabiriliriz vs. open felan diyerek fazladan karmaşıklık oluyor 
# bunları azaltmak için var olan bir sistem blok çalışır ve en sonunda otomatik olarak dosyayı kapatır ve çıkar
    

# read() fonksiyonunun içine yazdığımız rakam a kadar okuyordu bunu 5 ten sonrasını oku demek için ne yapmalıyız bunun içinde seek metodu var
    Dosya.seek(8)
    print(Dosya.read())
    # Çıktıda gördüğünüz gibi seek ile Merhaba yazısını atlayarak okuttuk   
    print(Dosya.tell()) # kaçıncı karakterde kaldığımı söyler mesela seek ile 8 karakteri atladık, read ile de 3 tane okuduk diyelim
    # toplam da 8 + 3 = 11 oldu yani imleç 12de şuan diyerek 12 döner. Burada yaptığımız işlemler ile 126.da kalmışız. 


with open("Merhaba.txt","r+") as dosya: # burada r+ ile sadece okumanın yanında ek olarak yazma işlemi de yapabiliyoruz. Normalde w kullansak siler
    # baştan yapardı biz bu durumdan kurtulmak için burada r+ kullanabiliriz. 
    dosya.seek(127) # burada 199 karakter sonrasında başla dedim bunun nedeni ise
    dosya.write("Merhaba, benim adım Kemalettin Kara.") # burada 199 u dan diye belirtmesem 0. karakterden başlayarak üstüne yazarak ilerlerdi ve 
    # önceki yazıları bozardı.
    dosya.seek(0) # yazma işleminden sonra imleç son kaldığı yerde durur ve read okumaz o yüzden 0 a çektim böylece gördük ki yazmış
    print(dosya.read()) 

with open("Merhaba.txt","a+") as dosya: #bu mod ise tamamen güncelleme üzerine kullanılan bir yapıdır. 
    dosya.write("\nNasılsın ? ")
    dosya.seek(0)
    print(dosya.read()) #burada da seek metodunu kullanmanın mantığı aynıdır unutma daktilo gibi . 
    # burada a+ w den daha mantıklı ekstra olarak seek atmana gerek yok yeni yerden başlayarak eklemeye devam ediyo 
    # bu bir güncelleme işlemi yan isadece okurken seek ile imleci başa getirip baştan okutuyoruz. En çok kullanılanlardan biri
    # a+ ve r+ zaten bunu da unutmamak lazım. 