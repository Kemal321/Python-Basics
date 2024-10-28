'''''''''''''''''''''''''''''''''''''''''''DATA FİLTRELEME'''''''''''''''''''''''''''''''''''''''''''''''''
import pandas as pd
import numpy as np
import os

clear = lambda: os.system('cls') # terminali temizleme fonksiyonu oluşturdum ki kısım kısım takibi yapılabilsin her bir clear() i silince ardı gelsin

veri = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python\hisse.xlsx",)
print(veri.head()) # dataFrame.head(parametre=5) şeklinde çalışan bir fonksiyondur yani eğer bir değer verirsek baştan değer kadar örneklem getirir
# Eğer vermez isek baştan 5 tane varsayılan olarak değer getirir bir de tail vardır baş ve kuyruk olarak kelimelerin anlamına göre tersten yapar.
print(veri.tail())

'''
Filtreleme kısmında tablo üzerinden yine python daki gibi düz düşünerek halledeceğiz aslında örneklerle gidelim mesela 
veri adlı data framedeki ismi acsel olan veriyi bul onun dışındakileri false yap aynı matlabdaki gibi element wise işlemler olacak


'''
print(veri=="ACSEL") # çıktıda verinin içindeki tüm değerleri tek tek element wise dediğimiz yani öğe bazında filtreleme yapıyor.
print(veri[veri == "ACSEL"]) # çıktıda görüldüğü gibi acsel dışındaki değerler NaN olurken bir tek acsel acsel olarak kaldı
# 2.sinde NaN dönmesinin nedeni aslında şunu yaptık veri[True yi bul yazdır yok ise eğer NaN dön dedik] NaN Not a Number
# yani aslında bir if else bloğu gibi düşünmek lazım bir şart koşuyorum ve ona göre uyanları alıyorken uymayanları atıyoruz

#  buna göre mesela rastgele olarak veriler arasında 10 dan büyük değerleri yazdıralım 
# print(veri[veri>10]) bu satırı yaptığın an patladın demektir çünkü senin tablonda tüm değerler sayılardan oluşmuyor  hatta bazen hiç sayı olmayabilir
# o yüzden sayılardan oluştuğuna emin olduğumuz yerlerde bunu yapmamız gerekiyor ise yaparız. tabi veri ön işleme adımlarında bu gibi hataları 
# yok edecek işlemler yaptığımız için sorun olmayacaktır. Şimdi yukarıdaki veri[veri>10] u sadece sayıların olduğu yerde yapmak için daraltalım 
# bu noktada mesela kapanış tl sütununu kullanabiliriz peki nasıl düz düşün ilk olarak kapanış tl sütununu almam lazım 
print(veri[veri["Kapanış (TL)"]>10])   # burada kapanış tl sütununu aldım daha önceki indeksleme kısmında öğrendiklerimizle 

# burada | veya operatörü ve & ile birden çok koşulu lojik mantığa göre birleştirebiliriz. Tabi ki de morgan kurallarını unutmayın.
clear()
''''''''''''''''''''''''''''''''''''''''''''''''''''GRUPLANDIRMA İŞLEMLERİ'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# bazen çalıştığımız verilerde gruplandırma işlemine tabi tutmak gerekebilir mesela diyelim ki Urfa da yaşayan mühendisler veya diğer iller 
# karşılaştırma yaparken aslında bir grup ortaya çıktı urfalı mühendisler grubu ortaya çıktı. işte bu noktalarda nasıl gruplandırma yapacağız bunu 
# örneklerle not alarak açıklayacağım.

izmirVeri = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python\izmirKazalar.xlsx")
grupluVeri = izmirVeri.groupby("TUR")
print(grupluVeri.groups)
'''bu şekilde kısaca gruplandırma yapabiliriz sonrasında tabi ilk olarak groupby bir obje döner biz bu obje üzerinden groups diyerek grupları ve 
kazaların indexlerini içeren bir dict alabiliriz. Bunun yanında grt_group diyerek de istediğimiz bir grup türünü alabiliriz. Mesela kazalara baktık
Lastikten dolayı olan kazalara bakalım.
'''
print(grupluVeri.get_group("Patlak Lastik")) # istersek tümünü groupbydan çıkan nesne üzerinden bir for döngüsü döndürerek de tüm kazaları yazdırabiliriz

# ilerlemek gerekirse mesela bu lastik patlamasından dolayı olan kazaları cadde istikametine göre sınıflandıralım 
PATLAKL = grupluVeri.get_group("Patlak Lastik").groupby("ISTIKAMET")
print(PATLAKL.get_group("Bornova")) # bu şekilde yeni örnekle başka şeylere bakalım