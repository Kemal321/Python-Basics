'''
JSON a başladık açılımı javascript object notation yani javascriptin bir nesne dönüşümü denen bir yapısı özel bir yapıdır ve her yerde kullanılır
genel olarak js için geliştirilmiş ama aktif olarak her yerde kullanılır yani. Yani anlaşılacağı üzere dilleri birbirine bağlayan ortak bir veri
yapısını oluşturarak bunları taşımaya çalışan bir yapıdır diyebiliriz. yani iletişimi sağlıyor. bir app yaptık diyelim bunu web sitesine entegre 
etmek istiyorsak bunu kullanarak yapıyoruz. 

Genel olarak stringlerden oluşuru zaten dict yapısı gibi olur genelde. Vs code conf dosyalarına bakarsan anlarsın. örnekle başlayalım

'''

#bir sözlük oluşturalım
bilgiler = {"Ad":"Kemal", "Soyad":"KARA", "Yas":25}
print(bilgiler["Ad"])
'''
Mesela burada başka bir dile bu bilgileri götürsek anlamaz mesela c++ da dict yapısı yok o yüzden bunu json a dönüştüreceğiz ve öyle kullanacağız
modülünü kendi adı ile import edelim
'''
import json
import os

path = r"C:/Users/Kemalettin/Desktop/Anlaşılır Ekonomi/Python/bilgiler.txt"

bilgiler = """{"Ad":"Kemal", "Soyad":"KARA", "Yas":25}"""
BilgiOku = json.loads(bilgiler)
print(type(BilgiOku)) # mesela çıktı artık bunun bir dict olduğunu söylüyor oysa o bir string ifade idi json.loads() ile bunu bir json a dönüştürdük
print(BilgiOku["Ad"]) # artık çıktı veriyor :d

# Bunu kullanarak kayıtlı dosyadan bilgi alalım mesela

with open(path,"r") as Dosya:
    # daha önce loads dedik şimdi load kullancaz bir yerden yükleme yaparken load() kullanılır 
    cevir = json.load(Dosya)
    print(cevir) # mesela bütün bilgiler artık sözlük tipinde elimizde olmuş oldu buradan bir kaçtane çağıralım mesela
    print(cevir["isim"]) #ahmet çıktısını aşağıda gördük. 

''' 
Diyelim ki burada elimizdeki bir bilgiyi json a atmak istedik nasıl olacak hemen ona bakalım bu noktada dumps() fonksyionunu kullanacağız
json.dumps()
'''
 
Bilgiler = {"Ad":"Mehmet", "Soyad":"TAKA", "Yas":23}
cevir = json.dumps(Bilgiler)   # eğer bir dosyaya oyollayacaksak dumps diyoruz 

with open("C:/Users/Kemalettin/Desktop/Anlaşılır Ekonomi/Python/bilgiler2.txt","w",encoding="utf-8") as Dosya:
    # klasik artık anladın dumps içerideydi yollarken ise dump kullancem
    json.dump(cevir,Dosya) # burada yukarıda hazırladığımız sistemi bilgiler2.txt diye bir dosya oluşturup oraya yolluyoruz. 
