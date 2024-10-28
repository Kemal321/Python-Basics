'''
Veri analizi Veri önişleme gibi işlemleri gerçekleştirmek için kullanılan bir kütüphane kısaca anlatacak olursak. Zaten tabanımız var 
tekrar mahiyetinde izliyoruz.... 
'''
import pandas as pd
import os
clear = lambda: os.system('cls')
'''
İçinde iki farklı veri türü bulunur 
1- Seriler - Pythondaki listelere benzer
2- Data Frameler 
'''
# inceleyerek başlayalım
seri = pd.Series() # bu şekilde bir seri oluşturuyoruz
print(seri) # Series([], dtype: object) şeklinde bir çıktı verdi [] -> Pythondaki listeleri hatırlatıyor :)

tamSayılar = pd.Series([1,2,3,4]) # tam sayılardan oluşan bir seri
ondalıkSayılar = pd.Series([0.1,0.2,0.3,0.4]) # ondalık sayılardan oluşan bir seri
karakter = pd.Series(["Merhaba","Benim","Adım","Kemalettin"]) # Karakter dizilerinden oluşan bir seri
karışıkSeri = pd.Series([1,"Kemalettin",0.1,"Çalış","Yoksa Paslanırsın"]) # sadece tek tip olmak zorunda değil farklı veri tiplerinide tek yerde tutar
print(tamSayılar,ondalıkSayılar,karakter,karışıkSeri,sep="\n")
'''
Çıktılarında dtype zaten numpy dan hatırlıyoruz data type bilgisini veriyor tek tip veri tipinden oluşuyorsa o veri tipini dönüyor 
farklı veri tiplerinde veri var ise dtype: object diyerek dönüş sağlıyor. Ek olarak çıktı alırken sol tarafta 0 1 2 diyerek giden
bir yapı var bu da listelerdeki indeks aslında serilerde indeks yapısı direkt olarak dönüyor. Jüpiter gibi defterlerde çalıştığınız
zaman direktmen tablo şeklinde bir gösterim oluyor merak edersen unutursan öyle de kontrol edebilirsin.
'''

# farklı veri yapılarından veya dışarıdan bilgi alarak da yapılabilir mesela
listem = [1,2,3,4,5,"Kemalettin"]
serim = pd.Series(listem) 
print(serim)
'''
# burada direkt olarak bir listeyi baz alarak bir seri oluşturduk bu tam bir dış kaynak olmasa da tamamen dışarıdan
# bir dosyayı da import ederek çalışabiliyoruz. Pandas numpy a göre daha esnek, daha güçlü ve daha fazla fonksiyon barındırıyor
veri analizi kısımlarında bizim için çok güçlü bir araç.
'''
# esneklikten bahsettik mesela bir sözlükten baz alarak seri oluşturduğumuzda serinin indeksleri sözlüğün key değerleri olur 
sozluk = {"Kemalettin":1,"Ahmet":2}
seriDict = pd.Series(sozluk)
print(seriDict)
#daha esnek
seri = ["Kemal","EsnekSeri"]
esnekSeri= pd.Series(seri,["Kendi","indexim"]) # dict verirsek nan oluyor dikkat. indeksler de bizim 2.parametremiz oldu
print(esnekSeri) # Seri oluştururken verilen 2.parametre ile kendi indeximizi de seçebiliriz ve veri tipi sayı olmak zorunda değil

del seri,esnekSeri,listem,serim,tamSayılar,karakter,karışıkSeri,ondalıkSayılar,seriDict,sozluk
clear()
x = pd.Series([1,2,3,4,5])
print(x.kurtosis()) # sum mean var std gibi numpy daki istatistik fonksiyonları burada da vardır ek olarak farklı fonklarda eklenerek güçlü
# bir yapıya evrilmiş pandas kütüphanesi mesela kurtosis() yani bir olasılık dağılımındaki basıklık veya sivrilik anlamına gelir pandas da
# bunun gibi bir çok ek fonksiyon veri analizi için eklenmiştir. 

# örneğin 
zaman = [2015,2016,2017,2018,2019,2020,2021]
veri = [3000,4000,5000,6000,7000,8000,9000]

seri = pd.Series(veri,zaman) # pd.Series(veriKümesi,İndeks) şeklinde çalışıyor unutmayalım
print(seri) #std sum mean gibi diğer fonkları bu seri üzerinde de uygulayabiliriz

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''DATA FRAMELER '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Bir nevi birden fazla serinin bir yapı içerisine toplanması ile oluşan yapıya data frame yani veri çerçevesi denir. Çeviri versiyonuda bu şekilde 
# tam olmuş oluyor sanırım. Şimdi teorik bir örnek görelim
seri1 =  [1,2,3,4,5,6]
seri2 = [1,2,3,4,5,6]
# bu iki seriyi tek bir dataFrame de toplayalım 
baslikliVeri = dict(Ürün1=seri1,Ürün2=seri2)
df = pd.DataFrame(baslikliVeri)
bosdf = pd.DataFrame()
print(baslikliVeri,df,sep="\n") # 
print(bosdf) # boş bir dataFrame nasıl görünür

clear()
# aslında numpy gibi düşünmek lazım yani satırları indeksliyoruz ve sütunları indeksliyoruz bu kadar aşağıdaki örnekle daha iyi anlaşılır 
df2 = pd.DataFrame([["Elma",10],["Armut",20],["Üzüm",30]],columns = ["Ürünler","Fiyatlar"]) # satırları oto indeks e bıraktım sütunları columns=
                                                                                             # diyerek ideksledim
print(df2)
# örneği açacak olursak 

veri = [["Elma",10],["Armut",20],["Üzüm",30]]
sutunIndeks = ["Ürünler","Fiyatlar"]
satırIndeks = [1,2,3]
df3 = pd.DataFrame(data=veri,columns=sutunIndeks,index=satırIndeks)
print(df3) 
#bu şekilde açıkça görülüyor ki tek yaptığımız indeksleri ayarlamak, numpy ın daha ui lı versiyonu gibi 

# Dışarıdan veri okuyarak yapmaya başlayabiliriz 2 adet örnek example.csv ve example.xlsx dosyamdan veri çekerek data frame olarak gösterelim
veri1 = pd.read_csv(r"C:\Users\Kemalettin\Desktop\anlasekon\Python\example.csv")
veri2 = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python\example.xlsx") 
# veri2 excel olduğu için kütüphaneye ek paketler indirmemiz lazım bunlar openpyxl xlsxwriter xlrd paketlerini yüklememiz lazım ilk 
# ben yükledim sizde hata verirse pip install openpyxl xlsxwriter xlrd diyerek yüklemeniz lazım

print(veri1,veri2,sep="\n")
# tabi iki yapı da aynı zaten o yüzden verileri aynı sadece tipleri ve kayıt edilme şekilleri farklı maksat görmüş olalım diye 
# en önemlileri csv excel json vs. zaten görmüş olmak iyidir.