##Bazı çok kullanılan ve bilinmeyen metodlardan bahsedeceğim
x = 2.3 
print(x.as_integer_ratio())  # bu hangi iki sayıyı bir birine bölersek x i elde ederiz değerlerini tuple olarak döndürür
print(x.__abs__()) #abs(x) olarak da kullanılır mutlak değer alır
print(x.__pow__(3)) # pow(sayı, üs) şeklinde de kullanılır üs alır 
print(x.__divmod__(3)) # verdiğimiz sayıya x i böldüğünde bölüm ve kalanı tuple olarak döner
print(x.is_integer()) # Tam sayı olup olmadığını sorgular ama 2.0 da bir tamsayı kabul edilir 


############### Karakter Metodları ##############
x = "Kemalettin"
x.lower() # hepsini küçük harfe çevirir
x.upper() # hepsini büyük harfe çevirir
x.islower() # hepsi küçük mü değil mi diye kontrol eder
x.isupper() # hepsi büyük mü değil mi diye kontrol eder

y =" 34342"
print(y.isnumeric()) # sayılardan oluşup oluşmadığını kontrol eder ama int float şeklinde değil string in içinde nümerik varsa bile kabul eder
print(y.isalnum()) # alfa nümerik yani sayı ve alfabe dışında bir değer kullanılıp kullanılmadığını sorgular 

z = "kemalettin reis. nasılsına"
print(z.capitalize()) # bu fonksyion stringin ilk harfini büyütür
print(z.title()) # her bir kelimenin ilk harfini büyük yapar 
print(z.swapcase()) # büyükleri küçük küçükleri büyük harf yapar 
print(z.count("A")) # verilen harfi string içinde sayar
print(z.strip("a")) # belirtilen karakterin başta ve sonra bulunuyorsa bunları kaldırır strin.strip() şeklinde de uygulanır 
print(z.lstrip(), z.rstrip()) # sadece bir yöne doğru kontrol etmek istersekde bu şekilde yaparız 
print(z.split(" ")) # string içinde verilen değeri gördüğü zaman onu böler ve liste şeklinde döner yani string = a b c string.split(" ") -> ["a","b","c"]
                    # şeklinde dönüt verir 

x = z.split(" ") # boşluklardan böldük diyelim 
print(x)
y = " ".join(x) # bu fonksişyonda verilen değerdeki her bir parçayı boşluk kullanarak birleştirir
print(y)

y2 = "eski parçalar geldi"
y2 = y2.replace("eski","yeni") # 2 parça alır ve eskileri yenilerle değiştirir gibi düşünün 
print(y2)

### En çok kullanılan metodlardan biri de format metodudur. Normalde c++ gibi dillerde std::cout << isim << diyerek ekleme yaparak devam eder
# pythonda ise 
Ad  = "Kemalettin"
Soyad = "KARA"
Meslek = " Kafaya göre"
print("Kişinin adı: {}, Kişinin soyadı: {}, Kişinin mesleği: {}".format(Ad,Soyad,Meslek)) # tabi ilaa bu şekilde değil diyelim bir liste var 
                                                                                          # oradan da çekebiliriz değerleri .format(liste[indeks],liste[indeks2]... )
                                                                                          # gibi
print(f"Kişinin adı: {Ad}, Kişinin soyadı: {Soyad}, Kişinin mesleği: {Meslek}") # Şeklinde de yapabiliriz. 


#########Liste metodları#####################
listem = [1,2,34,"Kemalettin",3]
# Liste üzerinde bazı metodlar güncelleme işlemi gerçekleştirir ve yeni değişken atamasında uygulandıklarında boş liste dönerler örnekle görelim
liste2 = listem.append("Kemalettin ekledi ama olmadı ")
print(liste2) # Çıktıda none çıktısı veriyor çünkü append uygulandığı liste üzerinde işlem yaptı ve liste2 ye none verdi
eklenecekindeks = 3
eklenecekeleman = 4
listem.insert(eklenecekindeks, eklenecekeleman) #append sona ekliyordu insert ile istediğimiz indekse ekleme yapabiliriz 
print(listem)

# remove verdiğimiz elemanla ilk karşılaştığında onu siler appende benzer olan pop() ise patlatmaktan gelir son elemanı siler
listem.remove("Kemalettin ekledi ama olmadı ")
print(listem) #işte sırası ile son elemanın silindiğini görüyoruz
listem.pop()
print(listem)

listem2 = ["bu liste","ile"," genişletildi"]
# burada .extend() fonksiyonu ise verdiğimiz liste ile uyguladığımız listeyi genişletir yani ekler güncelleme yapar none dener eğer satır içi
# işlemlerde kullanırsak
listem.extend(listem2) # listem2 ile listem i genişletecez yani listem2 yi listem e ekleyeceğiz 
print(listem)
# Burada aynı işlemi toplama işlemi ile de yapabiliriz yani listem = listem + listem2 veya listem += listem2 dersek aynı şeyi yapar 
# stringlerde olan count burada da vardır verdiğimiz elemanı listenin içinde arar kaç tane varsa bize sayısını döndürür
print(listem.count(3)) # mesela burada hiç olmadığı için 0 döndü

# sıralama fonksiyonları vardır sort() ve reverse()
#isminden belli zaten sort küçükten büyüğe veya tersi şeklinde sıralar, reverse ise tersine çevirir
listem3 = [1,2,5,23,25,3,3,3,6,32,345,65]
print(listem3) #burada reverse iç parametrelerden biri küçük büyük büyük küçük anahtarlama için
listem3.sort(reverse=False)
print(listem3)
listem3.reverse()
print(listem3)

listem3.clear()
print(listem3 , "Listem3 clear() metodu ile temizlenmiş yani içi silinmiş oldu")

# demetler yani tupleler için 2 fonksiyon bilmek yeterli 
demetim = (1,2,43,2,3,32)
print(demetim.index(3)) # verilen elemanın indeksini döner
print(demetim.count(2)) # verilen eleman demetin içinde kaç kere geçer bunu döner

########################################SÖZLÜK YAPISI ####################################################
Bilgiler = {"Ad: ": "Kemalettin",
            "Soyad: ": "KARA",
            "Yaş: ": 25,
            "Meslek: ": "Eng."
            }
print("Bu benim sözlüğüm:: ",Bilgiler)
# keys() ve values() kilit ve değerleri liste şeklinde döndürür örneğe bakalım 
print(Bilgiler.keys(),"Keys döndü\n",Bilgiler.values(),"Values döndü")
# Bir de items() vardır o da bu iki değerleri item olarak görür ve bunları döndürür
print(Bilgiler.items())
# Belirli bir key değerini alamk istersek get() fonksiyonunu kullanırız
print(Bilgiler.get("Ad: ")) # Kemalettin çıktısını verecek
# Sözlüğe yeni ekleme ile güncelleme yapabiliri bunun için update() kullanılır
Bilgiler.update({"Cinsiyet: ":"Errkek"})
print(Bilgiler) # Burada eklenmiş oldu 
print(Bilgiler.update({"Cinsiyet: ":"Errkek"})) # Güncelleme işlemi yaptığı için aslıda mantık olarakda none döndürdü
# Bilgiler.copy() diyerek kopyalşama işlemi yapabilriz 
Bilgiler2 = Bilgiler.copy()
# len() ile uzunluğunu da alabiliriz 
print(Bilgiler.__len__(), len(Bilgiler)) # ikiside aynı şekilde çalışır biri ekleme yapılan diğeri gömülü olan bir fonksyiondur

Bilgiler.pop("Cinsiyet: ") #Verdiğimiz key e bakarak o çifti silere 
print(Bilgiler)
Bilgiler.clear() # listelerdeki gibi çalışır 
print(Bilgiler)

################################Küme metodları###############################

kümem = {1,"Kemalettin",2.54}
kümem.add("Merhaba") # Eleman eklemek için kullanılır çoğu metod aynı zaten indeksleme olmadığı için de karışık gözükür unutma
print(kümem)

# Eleman silmek için de discard ve remove fonksiyonları var bunun temel farkı eğer silinecek eleman kümede yoksa 
# discar fonk. u hata mesajı döndürmezken remove döndürür 
kümem.discard("Merhab") # merhab yok merhaba var o yüzden boş bir dönüt vermesi lazım 
kümem.remove("Merhaba") # Burada ise key error döner o yüzden merhaba şeklinde değiştirdim ve kümem i yazdırınca merhaba silinmiş olacak
print(kümem)
###################Aritmetik - atama ve bazı karşılaştırma opertörlerini geçtim c c++ matlab hepsinde aynı şekilde çalışıyor biliyoruz zaten

# bir verinin olup olmadığını sorgulamak için kullandığımız operatör "in"
listem3 = [ 1 , 2 ,3 , 5]
print(3 in listem3) # True dönüyor çünkü 3 listede var. Çalışma mantığı basit 3 listede var mı diye soru sormak bu kadar 

# Bir de "is" yapısı var bu da aynı olup olmadığını sorgulamak için kullanılır aynı c++ deki pointer gibi her değişkenin bir id değeri var 
# Karşılaştırma işlemi bu id üzerinden yapılır 

s = [1]
y = [1]
print(s is y) # false döner çünkü id ler aynı değil id() fonksiyonu ile id lerini sorgulayabiliriz
print(id(s), id(y)) # çıktıya bakarsak id lerinin farklı olduğunuı görmüş oluruz == ise değer olarak karşılaştırma yapar farkı bu kadar 

# mantık operatörleri aynı şekilde geçiyorum and, or, not, Bu kadar yeni kod dosyasında devam edelim ders 26 ya geldik