'''
Bu kod sitenin arka planında çalışan kodları alıp bunları istediğimiz şekilde ayrıştırma görevi görüyor. API hizmeti sağlamayan sitelerde 
veri kazıma işlemlerini gerçekleştirme için bize yardımcı olacak. 

'''
from bs4 import BeautifulSoup
import os

kod ="""<!doctype html>
<html>
<head>
<meta charset="utf-8">
    <title>Liste Örnekleri-1</title>
</head>
    <body>
    <ol>
        <li>
            SICAK İÇECEKLER
            <ol type="I">
                <li>ÇAY</li>
                <li>KAHVE</li>
                    <ol type="a">
                        <li>TÜRK KAHVESİ</li>
                        <li>NESCAFE</li>
                    </ol>
                <li>SICAK ÇİKOLATA</li>
            </ol>
        </li>
        
        <li>
            SOĞUK İÇECEKLER
            <ol>
                <li>MEYVE SULARI
                    <ul>
                        <li>Vişne</li>
                        <li>Şeftali</li>
                        <li>Kayısı</li>
                        <li>Elma</li>
                    </ul>
                </li>
                
                <li>
                    LİMONATA
                </li>
            </ol>
        </li>
    </ol>
    
    </body>
</html>"""

parset = BeautifulSoup(kod,"html.parser")
yaz1 = parset.prettify() # bu fonksiyon daha düzgün bir şekilde görmemizi sağlamak amacıyla çalışır
yaz = parset.title # bu şekilde etiketleri de çekebiliriz mesela parset.title.name yaparsak direkt olarak o etiketin adını çekecektir
#print(yaz)

yaz2 = parset.body
#print(yaz2)

# sitenin adını çekmeye çalışalım mesela
yaz3 = parset.title.string
#print(yaz3) # Liste Örnekleri-1 şeklinde bir bilgi dönüyor mesela bu direkt olarak title da bulunan string anlamındadır 
'''
Burada tabi yapıyı baştan aşağı tanımaya başladığı için bu noktada ilk karşılaştığı etiketi pars eder.  Tamamını bulmayı da yapabilirz

'''
yaz = parset.find_all("li") # mesela liste veri tipinin içine alarak bunları bize döndürdü bu noktada indexlerle kendi elimizle de parse edebilriz#
#print(yaz)

# yani burada nokta ekleme nokta ekleme gibi devam etcez yani mesela yaz = parset.find_all("li").ol.find_all("li") mesela burada ol o bölümün
# tamamını alırken find_all ile de sıcak içecekler kısmındaki li lerin hepsini find et yani bul yaptık ve getirdik
# aslında düz bir grup hiyerarşisi var 
yaz = parset.li.find_next_sibling() # aynı buradaki gibi aslında bir aile yapısı ile buluyor indentler ile de bunu takip edebiliriz. 



####################################################################################################################################
############################################### IMDB VERİ KAZIMA ###################################################################
'''
iLK OLARAK videodaki gibi verinin kazınacağı siteyi iyice hakim olmalıyız yani kazımak istediğimiz veriler sitenin neresinde 
hangi etiketler arasına yerleştirilmiş hangi yolla bunu ayıracağımızı bu etiketlerin dizilimine bir biri içinde 
nasıl bir hiyerarşi oluşturduğuna bağlı olarak bunları bilebiliriz. 

'''
import requests
from bs4 import BeautifulSoup

link = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

kod = requests.get(link,headers=headers).content

#kod = baglan.content # burada content diyerek aslında sayfa kaynağını incele dediğimizde arka plandaki tüm kodları çekmiş olduk
parserim = BeautifulSoup(kod,"html.parser")

# daha önce sayfayı inceledik ve orada tbody arasında olan filmleri çekeceğimiz için oraya ilerleyeceğiz.

li = parserim.find("ul",{"class":"ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 dHaCOW compact-list-view ipc-metadata-list--base"}).find_all("li") # bu tümünden ilkini çeker bu bizim çok işimize yaramaz çünkü sitede ul olan yüzlerce olabilir biz class ı ile vs.
# kendini diğerlerinden ayıranı bulacağız o yüzden find() yapısını kullanacağız. 

for i in li:
    a3 = i.find("h3",{"class":"ipc-title__text"}).string
    print(a3)

#h32=tr.find("h3",{"class":"ipc-title__text"})
#print(h32)



