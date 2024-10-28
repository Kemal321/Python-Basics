import pandas as pd
import numpy as np
'''Bu derste bir çok sayfaya sahip excel dosyalarını nasıl çekeceğiz bakacağız edeceğiz onu çalışacağım'''
veri = pd.DataFrame(pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python\Hastanenorm.xlsx"))
# bunu bu şekilde çalıştırdığımızda sadece ilk sayfayı alır diğer sayfaları almak için ekstra bir parametre vermeliyiz. sheet_name diyerek
veri = pd.DataFrame(pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python\Hastanenorm.xlsx",sheet_name="Doktor"))
print(veri) # görüşdüğü üzere doktor sheetinin bilgilerini çekmiş oldu 
# aynı zamanda excel aslında bir dataframedir oradaki sayfalarda aslında birer indekslemedir buna göre biz istersek direkt olarak indeks sayısı da
# verebiliriz 
veri2 = pd.DataFrame(pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python\Hastanenorm.xlsx",sheet_name=4))
print(veri2) # veri ile aynı şeyi yani doktor sayfasını yazdırdı düz indeks kullanmamıza rağmen çalışıyor çünkü her biri aslında sadece indeks


#  peki belki excel de 199349 tane sayfası olan bir excele denk geldik o zaman ne olacak bunun için ExcelFile diye bir fonksiyon ile excel
# dosyalarını kontrol edebilmemiz için pandasda ekstra fonksiyon var 

veri = pd.ExcelFile(r"C:\Users\Kemalettin\Desktop\anlasekon\Python\Hastanenorm.xlsx") # çıktı olarak bir obje verir bu obje üzerinden metodlarla
# çalışacağız mesela sheet names i alallım 
print(veri.sheet_names) # ['Hasta', 'Ulke', 'il', 'İlce', 'Doktor', 'Kan', 'Bolum', 'Kurum'] çıktısını verdi ve liste verisi olarak döndü
# bunu kullanarak düzgünce okuma yapabilir miyiz
veri2 = pd.DataFrame(pd.read_excel(veri,sheet_name=veri.sheet_names[0]))
print(veri2) # gördüğünüz gibi bunu kullanarak okumaları ve diğer sayfalara da bunun üzerinden ulaşabiliyoruz
# beyin fırtınası yaparak neler yapabileceğimizi düşünün döngülerle tek tek sayfalar arasında dolaşabiliriz onları otomatize bir sistem haline 
# getirebiliriz bir modüler oop ile class ları kullanarak yani bir sistem oluşturabiliriz vs. vs.

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''PANDAS İLE PİVOT TABLE'''''''''''''''''''''''''''''''''''''''''''''''''''''
# Excelde var olan pivot table özelliği burada da var zaten ikisi neredeyse aynı şeyler demiştir nasıl kullanacağımıza geçelim hemen 

#veri5 = pd.DataFrame(pd.read_excel("hastane.xlsx"))
#veri2=veri5.pivot_table(values="Yas",columns="Cinsiyet",aggfunc=sum) # bu kadar excel de var olan değerler kısmı values sütunda diğer kısım zaten 
# aggfunc aggregate function demek o da uygulanacak fonksiyon toplamak ortalama almak vs. herşeyi uygulayabiliriz. 
# sütun satır ne varsa uygulanır aynısı daha fazla not almak istemiyorum bu konu için çünkü excelin aynısı 


'''''''Peki excelden buralara geldik ama buralardan excele gidemez miyiz tabi gidilir onu öğrenelim'''''''

seri1 = pd.DataFrame({"Ad":["Ebubekir","Ömer","Osman","Ali"],
                      "Soyad":["Sıddık","Faruk","Zinnureyn","Esedullah"]})

seri2 = pd.DataFrame({"Şehir":["Medine","Kudüs","Rakka","Mekke"],
                      "Sıcaklık":[41,42,43,44]})

print(seri1)
print(seri2)

#güzel dataframelerimizi oluşturduk

#dosya = seri1.to_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python\pyToExcel.xlsx",sheet_name="Ad_Soyad") # to_excel veya diğer varyasyonlarla bu şekilde oluşturuyoruz
# kontrol ettim güzelce oluşturmuş ve yapıştırmış. İndeksleri de alıyor bunu istemiyorsak parametrelerde index = False yapmamız yeterli
# şimdi ikinci dataframeyi de almak istiyorsak ne yapmamız gerekiyor. şimdi onu görelim to_excel dosyaların write metodu gibi çalışır 
# o yüzden with ile yapmamız lazım 
with pd.ExcelWriter(r"C:\Users\Kemalettin\Desktop\anlasekon\Python\pyToExcel.xlsx") as writer:
    seri1.to_excel(writer,sheet_name="Ad_soyad",index=False)
    seri2.to_excel(writer,sheet_name="Hava",index=False)
# düzgünce eklenmiş oldu, burada tek mevzu her hangi bir yerden dataları dataframe yapısında oluşturmak bu kadar 
# sonrasında dosya yönetimi ile aynı şekilde çalışıyor zaten
    

# bir örnek yapalım 110.video sonrasında kendi örneklerimizi yaparız. 
seri = pd.DataFrame(pd.read_csv(r"C:\Users\Kemalettin\Desktop\anlasekon\Python\trcar.csv"))

# dosyayı xlsx e kaydedelim tek olduğu için direktmen yapacağız 
seri.to_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python\trcar.xlsx",index=False)

seri2=pd.DataFrame(pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python\trcar.xlsx"))

# ne kadar uzunluğu olduğunu öğrenelim
print(seri2.index)

# hangi kolonlara sahip onu öğrenelim yani sütun başlıkları
print(seri2.columns)

# Genel olarak sütunlar hakkında bilgi almak istiyorsak 
print(seri2.info())


# Fiyata göre artan sırada sıralayarak yazdırdık. Burada indeks ve değere göre sıralama yapabiliriz zaten index default ise anlamı olmaz :)
print(seri2.sort_values("Fiyat")) 