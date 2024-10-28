'''
Numerical Python yani sayısal işlemleri yapacağız yani matrixlerle çalışacağız burada 
Paralele hesaplama için genellikle yapay zeka işlemlerinde matriks işlemleri ile paralel hesaplama yaparız 
bu bize hem hız hem de kullanım kolaylığı sağlar. 
'''

import numpy as np

dizi = np.array([1,2,3,4,5,6,7]) 
print(type(dizi)) # dikkat edersen çıktı olarak ndarray tipinde çıktı verdi

cokBoyutluDizi = np.array([[1,2],[3,4],[5,6]]) 
print(type(cokBoyutluDizi),dizi,cokBoyutluDizi,sep="\n") #çıktıda çok boyutlu dizi bir matris olarak döndü class olarak yine numpy.ndarray

# mesela boyutu almak için shape metodunu kullanabiliriz
print(cokBoyutluDizi.shape) #( 3, 2 ) şeklinde bir tuple döndü 3 satır sayısı iken 2 sütun sayısını temsil ediyor.

# ek olarak aynı matris üzerinden yeni matrisler üretirken de farklı boyutlandırma da yapabiliriz bunun için reshape fonksiyonu kullanılır 
yeniBoyut = cokBoyutluDizi.reshape(1,6) # eleman sayısı 3x2 den 6 tane oldğu için 1x6 oluşturmak istiyorum 
print(yeniBoyut,type(yeniBoyut)) # aynı class fakat artık 1x6 lık bir matris üretmiş olduk

# elemanlarının tipini öğrenmek için ise dtype metodundan yararlanabiliriz
print(yeniBoyut.dtype) # mesela burada int64 olarak döndü aynı şekilde farklı türleride içine alabilir listeler gibi 

'''Farklı türlerde diziler oluşturabiliriz bu şekilde örnek ile görelim'''
dizi1 = np.array([1,2,3,4,5],dtype=int)
dizi2 = np.array([1,2,3,4,5],dtype=float)
dizi3 = np.array([1,2,3,4,5],dtype=complex)
dizi4 = np.array([1,2,3,4,5],dtype=str)
dizi5 = np.array([1,2,3,4,5],dtype=bool)


print(dizi1,dizi1.dtype)
print(dizi2,dizi2.dtype)
print(dizi3,dizi3.dtype)
print(dizi4,dizi4.dtype)
print(dizi5,dizi5.dtype)

# bu şekilde eleman tipini de oluştururken dtype ile belirlemek için kullanabiliriz 

# tamamen bir lerden oluşan veya sıfırlardan oluşan matrisler oluşturmak için özel fonksiyonlarımız mevcut bunlar ones ve zeros
sıfırlar = np.zeros((3,3),dtype=int) # bu (3,3) lük 0 lardan oluşan veritipi int olan bir matris oluştur demek 
birler = np.ones((3,3),dtype=int) # bu (3,3) lük 1 lerden oluşan veritipi int olan bir matris oluştur demek

print(sıfırlar,birler,sep="\n")
# bunlar nerede kullanılır belirli tipte bir matris ihtiyacımız olursa hızlıca bu şekilde oluşturabiliriz. Mesela 10 farklı tür var veya 
# yarışmacı var 10 tane counter tanımlamamız gerekiyor o zaman toplu olarak counter tanımlamak gibi düşünebiliriz. 
# Mesela 10 lardan oluşan üretmek istiyoruz o zaman da 1 lerden oluşanı 10 ile çarparak düz mantıkla üretebiliriz. 

onlar = birler*10 # bunun için fornksiyon da bulunmakta tqabi
onlar2 = np.full((3,3),10)
print(onlar==onlar2) # bu şekilde ilerleyebilir. 


# bir birim matris oluşturmak için eye() fonksiyonunu kullanılırız
birimMatrs = np.eye(5,4) # burada k diye bir 3. bir parametre de verebiliriz bu kaçıncı sütundan 1 leri koyacağını belirler. 
# eye(3) diye bırakırsak ise diretk olarak 3,3 yani bir kare matri oluşturur. 
print(birimMatrs)

# Köşegenlerinde 1 den farklı sayılar olsun istersek o zaman diag() fonksiyonunu kullanabiliriz
farklıBirim = np.diag([1,2,3,4,5,6,7]) # 7,7 lik bir kare matris oluşturur ve birim matris yerine diagonalında bu sayılar olur 
print(farklıBirim)

farkliRange = np.arange(0,100,5) # matlabdaki linspace fonksiyonuna benzer [sayı,sayı,adım) aralığında adım kadar artarak sayıları bir array yapıyor
print(farkliRange,type(farklıBirim))

# matlabdaki linspace burada da var zaten muhtemelen buradan geçmiştir bu verilen aralığı istenilen eleman sayısına göre ayarlıyor 
# yani mesela (0,100,5 ) demek burada 5 adım değil eleman sayısı yani 0-100 arasını eşit aralıkta bölerek 5 eleman seç demek 
# buradaki mesele linearly spaced kelimelerinin birleşiminden doğan bir fonksiyon aslında.

farkliSpaced = np.linspace(0,100,5) # burada son aralık dahilidir istemiyorsak endpoint parametresine false vererek kapatabiliriz. 
print(farkliSpaced)

# rastgele sayılar içni

# numpy da random kütüphanesi eklenmiş ve matris üretebiliyoruz. 
rastgele1 = np.random.randn(3,3) # bu mean ı 0 varyansı 1 olan normal dağılıma göre dağılmış rastgele sayılardan oluşan bir matris döner. 3e3 lük
print(rastgele1)

rastgele2 = np.random.randint(0,10,size=(3,3)) # bu fonksiyon ise üsttekinden farklı olarak ilk 2 parametreye göre başlangıç ve bitiş arasından rastgele sayı üretir
print(rastgele2)

'''
Array indeksleme liste indeksleri ve matlabın aynısı sadece arrayler birer matriks olduğu için satır,sütun şeklinde bir yapıya sahip
o yüzden bilmemiz gereken bir bilgi var ekstra olarak arrayAdı[:,sütun], arrayAdı[satır,:] bu iki çağrı şeklinin mantığı aynıdır 
o da şudur ki : -> bu kısım tamamı demekti zaten , -> virgülden sonraki kısma yani satırdan sonraki kısmın infosunu vereceğim demek 
sütun veya satır bilgileri ise istenilen sütun veya satır bilgisi bu tüm satırı veya sütunu tek parça olarak çekmeye yarar. Matlab gibi
'''
# matristen eleman silmek için np.delete() fonksiyonunu kullanıyoruz np.delete(arrayAdı,silinecekElemanınİndeksi,(çok boyutlu ise satır mı sütun mu))
silme = np.arange(16).reshape(4,4)
silinenSatır = np.delete(silme,[0],axis=0) # silme arrayının 0.satırını sil ve kalanlarını silinen e ekle demek yani sonucu görelim
print(silme,silinenSatır,sep="\n")
silinenSütun = np.delete(silme,[0],axis=1) # bu sefer de axis = 1 diyerek sütun yok edeceğimi bleirttim ve 0.sütunu yok ederek kalanları tuttum
print(silme,silinenSütun,sep="\n")

# matrise eleman ekleme kısmı ise listelerde olduğu gibi burada da append() fonksiyonu kullanılır 
# np.append(arrayAdı,eklenecekEleman,(çok boyutlu ise axis = 0 satır, axis = 1 sütun işlemi))
ekleme = np.arange(9).reshape(3,3)
eklemeSütun =np.append(ekleme,[[100], [200], [300]],axis=1) # tabi bu iki boyutlu olduğu için sütunları eklerken ayrık olarak vereceğiz 
# çünkü bunların satırları farklı farklı satırlarda olduğunu belirtmemiz lazım yoksa dimension error alırız.
print(ekleme,eklemeSütun,sep="\n")
eklemeSatır = np.append(ekleme,[[100, 200, 300]],axis=0)
print(silme,eklemeSatır,sep="\n")

# python daki set yani küme işlemleri burada da vardır. Bunları kullanarak küme işlemlerinin avantajlarından yararlanabiliriz. 
array1 = np.random.randint(0,10,5)
array2= np.random.randint(0,10,5) # rastgele int lerden oluşan 2 array tanımladım kullanımı yukarıda var unutursan tekrar et

farkArray = np.setdiff1d(array1,array2) # bildiğin A / B yani A da olup B de olmayanları bulmak gibi 
print(array1,array2,farkArray,sep="\n")

birlesimArray = np.union1d(array1,array2) # bu da birleşim işlemi için ekstra olarak birleştirdikten sonra sıralı bir biçimde yeni array yapar
print(array1,array2,birlesimArray,sep="\n")

print(np.isin(array1,array2)) # eski adı np.in1d idi çok saçma duruyordu intersection1d ile karışabilirdi, ismi isin diye değişti
# amacı array1 in elemanlarını tek tek array2 nin içinde mi sorusunu sormak ve cevabı tabi ki boolean olarak saklar 


# tekrarlayan verileri kaldırmak için bir fonksiyonumuz var np.unique() zaten kelimeden anlaşılacağı üzere unique yani tek olan eşsiz olan
# amacı o arrayda kullanılan her bir verinin sadece 1 kez geçmesini sağlayan arrayı dönmek 

print(np.unique(array1)) # bu elemanda indeksleri dönmesini de isteyebiliriz, sorted olarak döner zaten ek olarak bir çok özelliği vardır
# dökümantasyonuna bakarak kullanımını basitçe görebiliriz zaten. çok boyutlularda da kullanılır.

print(np.sort(array1)) # klasik sort eder istediğimiz gibi sort ettiririz. 

'''''''''''''''''''''''''''''''''''''''''BAZI KULLANILABİLECEK İSTATİSTİK FONKSİYONLARI'''''''''''''''''''''''''''''''''''''''''''''
'''
Temel bazda zaten toplama (np.add), çıkarma ( np.substract ), çarpma ( np.multiply ), bölme ( np.divide ) fonksiyonları var veya 
operatörler yardımı ile de yapabiliriz bunlara ek olarak 
'''
# np.min arraydaki minimum elemanı döner önveki array1 den devam edelim
print("Dizinin en küçük elemanı: ",np.min(array1),f"Array: {array1}")
print("Dizinin en büyük elemanı: ",np.max(array1),f"Array: {array1}")
print(f"Her bir elemanın kareköklü hali: {np.sqrt(array1)}")
print(f"Dizinin elemanlarının toplamı: {np.sum(array1)}",f"Array: {array1}")
print(f"Her bir elemanın log10 hali: {np.log(array1)}")
print("Dizinin ortalaması: ",np.mean(array1),f"Array: {array1}")
print("Dizinin medyanı: ",np.median(array1),f"Array: {array1}")
print("Dizinin varyansı: ",np.var(array1),f"Array: {array1}")
print("Dizinin standart sapması: ",np.std(array1),f"Array: {array1}") # zaten varyansın karekökü :D