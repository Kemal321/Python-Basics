'''

DataFrame Satır ve Sütun İşlemleri
Okunan dosya üzerinde ne gibi işlemler yapılır onlara bakacağım

'''
import numpy as np
import pandas as pd



veri = pd.DataFrame(pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python\hisse.xlsx"))
print(veri) # 573 adet hissemizin günlük haftalık aylık ve yıl içi getiri yüzdelerinin olduğu bir excel dosyası olduğunu gördük



# sütunları çekme
print(veri[["Kod","Kapanış (TL)"]]) #bu şekilde birden çok sütunu tek işlemde çekebiliriz parametre 1 den fazla olacağı için liste yaparak yolladık
print(veri["Kod"]) # tek bir sütunu ise dict içinde key ile arama yapar gibi yaparak da çekebiliriz 



# satırları çekmek için ise loc yani location ( indekse göre çekecez yani ) fonksiyonunu kullanacağız
print(veri.loc[0]) # bu şekilde 0.indeksteki verinin tüm satırlarını alt alta yazarak getirdi
print(veri.loc[[1,2,3,4,5,6]]) # aynı şekilde birden fazla çekmek içni liste gönderiyoruz
# aslında loc hem satır hem sütun için kullanılır mesela 5.indexin haftalık getirisini çağıralım
print(veri.loc[5,"Haftalık Getiri (%)"]) # 1.84 değerini dönmüş oldu aslında tam bir lokasyon almış olduk 
# fikir yürütürsek [satır,sütun] indeksleme işlemlerinin hepsini yapabileceğimiz anladık sanırım 
# print(veri.loc[0:3,0:3]) bu çalışmaz tabi indekslerimizin tipi yani farklı bir indeks yapısı kullandıysak ona göre kullanmamız lazım doğrusu
print(veri.loc[0:3,"Kapanış (TL)":"Aylık Getiri (%)"])



# Sütun ekleyelim 
# dict gibi ekleme yaparız
veri["Karekök Fiyat"] = np.sqrt(veri["Kapanış (TL)"])
print(veri) # sonuçta gördüğümüz gibi karekök fiyat bilgisi yeni sütuna eklenmiş oldu 



# bu metod diretk olarak append gibi sona ekliyor istediğimiz bir aralığa eklemek için insert() fonksiyonunu kullanabiliriz
veri.insert(2 , column = "Log Fiyat",value = (np.log(veri["Kapanış (TL)"]))) # insert(konum,column = Sütun ismi,value=Değer veriler yani)
# şeklinde çalışır, Bir de kalıcı olmayan ve kalıcı olan silme işlemlerini görelim
veri2 = veri.drop("Günlük Getiri (%)",axis=1) # axis = 0 satır 1 sütun için burada drop u bu şekilde kullanınca asıl veride kalıcı olmayan bir silme
print(veri2,veri, sep="\n")