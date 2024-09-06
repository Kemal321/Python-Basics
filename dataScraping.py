'''
Basit bir veri kazıma verinin kazınacağı site Vatan bilgisayar olarak seçilmiştir. Vatan bilgisayar sitesinin içinde bulunan telefon modelleri ve 
Fiyatlarını otomatik bir şekilde çekip düzenleyerek yazdıracak kodlar aşağıdadır. 
'''

import requests
from bs4 import BeautifulSoup
for sayfa in range(1,11):
    url = f"https://www.vatanbilgisayar.com/cep-telefonu-modelleri/?page={sayfa}"
    parser = BeautifulSoup(requests.get(url).content,"html.parser")
    main = parser.find("div",{"class":"wrapper-product wrapper-product--list-page clearfix"}).find_all("div",{"class":"product-list product-list--list-page"})


    for i in main:
        isim = i.find("div",{"class":"product-list__content"}).find("div",{"class":"product-list__product-name"}).find("h3").string

        fiyat = i.find("div",{"class":"product-list__content"}).find("div",{"class":"product-list__cost"}).find("span",{"class":"product-list__price"}).string

        print(f"Telefon Modeli: {isim}\nTelefon Fiyatı: {fiyat} ₺ dir.\n")