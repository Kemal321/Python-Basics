import json
import requests


'''
Yani request yapısı siteye bir talepte bulunuyor zaten istek diye çevrilebilir kelime anlamı da. Bu istek okeylenirse o zaman bu sitenin 
içindeki json veri türünde saklanan bilgileri alabilmemiz yani kazıyabilmemiz olanaklı olmuş oluyor. Böylece bizde veri kazımış oluyoruz.

'''

site=requests.get("https://jsonplaceholder.typicode.com/todos")
sitem = json.loads(site.text)

'''for i in sitem:
    print(sitem)'''

'''Burada da verileri json.loads() ile yükleyerek hepsini almış olduk böylece işlemi basit bir for döngüsü ile ekrana bastırmış olduk.'''

'''
yeni bir konuya gelmiş olduk arkadaş API bu application programming interface yani uygulama programlama arayüzü olarak çevirilebilir 
bir uygulamanın içindeki işlevsellerden bazılarının veya tamamının başka bir uygulama tarafından kullanılmasına izin verilmesi de denebilir 
mesela A uygulamaısnın özellekleri güzel bu uygulama başkaları da kullansın diye bir kaç özelliği sunuyor ve millet kullansın felan diyor 
mesela twitterdaki beğenme işlevi veya mesajlaşma işlevi gibi bunu sundu başkası da bunu kullanarak hızlıca beğenme veya mesajlaşmayı entegre 
edebilir. 
'''
############################################################ HAVA DURUMU UYGULAMASI YAPALIM ######################################################
APIKEY = "YOURAPIKEY"
while True:
    CITY = input("Hava durumunu öğrenmek istediğiniz şehri giriniz -->").capitalize()
    address = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=tr&units=metric".format(CITY,APIKEY)

    baglan = requests.get(address)
    sorgu = baglan.json()

    sicaklik = sorgu["main"]["temp"] 
    hissedilenSicaklik = sorgu["main"]["feels_like"]
    havaDurumu = sorgu["weather"][0]["description"]
    nem = sorgu["main"]["humidity"]

    print(f"{CITY} şehri için...\nSıcaklık: {sicaklik}°\nHissedilen Sıcaklık: {hissedilenSicaklik}°\nHava Durumu: {havaDurumu}\nNem: %{nem}\nŞeklindedir...")

