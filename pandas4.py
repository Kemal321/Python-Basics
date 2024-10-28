import pandas as pd
import numpy as np
import os
clear = lambda: os.system("cls")
veri = pd.DataFrame(pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\python\hastane.xlsx"))

# Cinsiyete göre gruplandırma
# Cinsiyete göre gruplandırdıktan sonra get group ile erkekleri aldım ve cinsiyet serisini aldım saydım bu kadar
Erkek = veri.groupby("Cinsiyet").get_group("Erkek")["Cinsiyet"].count() 
Kadın = veri.groupby("Cinsiyet").get_group("Kadın")["Cinsiyet"].count()

print(f"Erkek hasta oranı {( Erkek/(Erkek+Kadın) ) * 100}\nKadın hasta oranı {( Kadın/(Erkek+Kadın) ) * 100}")


# Gruplananların yapısı bozulmadığı için cinsiyetlere göre yaş ortalamalarını da alabiliriz
yaşOrt = veri.groupby("Cinsiyet")["Yas"].mean()
print(yaşOrt,type(yaşOrt),type(veri.groupby("Cinsiyet")["Yas"]))
# Name: Yas, dtype: float64 <class 'pandas.core.series.Series'> <class 'pandas.core.groupby.generic.SeriesGroupBy'>
# bakın tipini sorguladığımda yaş ort için bir seri olduğunu söylüyor diğeri için bir obje olduğunu daha detaylı bakalım

# birden fazla gruplandırma da yapabiliriz 
# daha önce olduğu gibi birden fazla vereceğimiz zaman liste olarak veriyoruz 
birden = veri.groupby(["Cinsiyet","İl"])["Yas"].mean()
print(birden)
# sonuç olarak il il kadın ve erkeklerin yaş ortalamalarını bulmuş olduk bu kadar 



'''''''''''''''''''''''''''''''''''''''''''''''''''''''İNDEKSLEME'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Bazen farklı bir indeksleme kullanmamız gerekebilir çünkü python'ın indeksleme sistemi yanlışlıkları farkedemeyebilir 
# mesela yukarıda cinsiyete göre count yapmak ile direktmen erkek üzerinden yapılan count farklı sonuçlar veriyor ya eksik veri var 
# ya da yanlış veri koymuşlar ya da taşma olunca işlem bozulmuş vs. herhangi bir şey olabilir. 
# bu yüzden bazı indeksleme işlemleri yapmamız gerektiğinde bazı fonksiyonlar kullanmamız lazım ilk olarak indeksi her hangi bir sütun olarak
# atayabiliriz ilk olarak bunu görelim 
veri.set_index("Tc",inplace=True) # her kişinin tc si 1 tane olarak o kişiye özel olmasından dolayı indeks olarak atamak istedim bunun için set_index fonksyionu
# kullanılır. Her hanhi bir sütunu indeks olarak atamak istersek o zaman set_index(parametre) yi kullanmamız lazım
#inplace= True Parametresi normalde false olarak belirlenir True yaparsak yaptığımız değişikliği orjinal veride de meydana getirir

# işlemi geri almak için reset_index() kullanılır 
print(veri.head())
veri.reset_index(inplace=True) # bununla beraber tekrar indekslemeyi 0 dan başlayarak normal haline getirdi
print(veri.head())
clear()
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''Pandas DataFrame NaN Değerler'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
veri2 = pd.DataFrame(pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\python\hastane2.xlsx"))
# ilk olarak boolean indekslemeyi görmüştük bunu null yani boş değerler için yapalım isnull ve notnull fonksiyonları var 
print(veri2.isnull()) # buradan null mu ? diye sormak aslında boolean indeksleme yani 
# çıktıya baktığımızda false ve trueler var olması gerektiği gibi yani True olan değerler aslında boşmuş tam tersini deneyelim bir de 
print(veri2.notnull())
# bunları sum fonksiyonuna vererk sayılarını da öğrenebiliriz böylece karşılaştıradabiliriz
print(veri2.isnull().sum(),veri2.notnull().sum(),sep="\n")
# çıktıya bakacak olursak toplam 14 satır vardı boş olanların sayısı ile boş olmayanların sayısını topladığımızda aslında hep 14 çıkıyor bu kadar.

# bu verileri doldurmanın bir çok istatistiki yaklaşımı var bunlara giremeyiz ilk olarak bu değerleri nasıl ortadan kaldırırız buna bakalım
# bunun içni dropna dediğimiz bir fonksiyon var yani drop düşür na not answered gibi bir kelime birleşimi aslında 

veri3 = veri2.dropna(axis = 0)# burada boş çalıştırırsak satırı siler axis i kullanmamız lazım alıştık zaten 0 satır için 1 sütun için 
print(veri3) # boş değer içeren satıları sildiğimiz için burada boş değer içermeyenleri yazdırdı 2 7 13 indeksli satırlarda hiç nan değer yokmuş

# istersek spesifik bir sütuna göre de silme işlemi yapabilriiz 
veri4 = veri2.dropna(subset=["Cinsiyet"]) # bunun için subset parametresine istediğimiz altkümeyi verdik ve ona endeksli bir şekilde kontrol yaptı
print(veri4) # bu sefer tüm veri geldi çünkü cinsiyet sütununda nan olmayan değer yokmuş ama diğer yerlerde hala var çünkü biz cinsiyete endeksli
# kontrol ettik, bir kaç sütunu verebiliriz subset = ["Cinsiyet","Yas"] diyerek birden çok yeri de kontrol ettirebilirz 

# tersinir olarak silebileceğimiz bir şey dolduradabiliriz fillna() fonksiyonu ile de doldurma işlemini yapabiliriz 

veri3 = veri2.fillna(value="Değer yok")# ister int ister str vererk bunları doldurabiliriz value = 1 veya value = "1"
print(veri3) # tabloda değer yok olarak dolduruldu