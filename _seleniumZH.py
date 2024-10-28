import time
from selenium import webdriver
from selenium import webdriver # bunu driver i çalıştırmak için bende chrome biraz arızalı çalışıyor o yüzden edgeye geçtim. 
from selenium.webdriver.common.keys import Keys # bunu enter tuşuna bas veya spaceye bas gibi komutları verebilmek için ekledik
import time # bekleme vs. koyuyorum ki komutların çalışmasını tam olarak görelim. Yoksa çok hızlı çalışır çalıştı mı bilemeyiz
from selenium.webdriver.edge.options import Options 
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
'''                              FELSEFE KİTAPLARINA GİDECEK VE ORADAKİ İLK 10 KİTABIN ADINI ÇEKECEK BİR UYGULAMA YAPALIM                  '''


# klasik bir şekilde options kurarak başlıyorum 
options = Options()
# hataları almamak için kullandığımız yapıyı çalıştıralım
options.add_experimental_option("excludeSwitches",["enable-logging"])

# Driverime ulaşmam gerek o yüzden path yollarını hazır ettim. Edge WebDriver'ın dizin yolu
driver_path = r"C:\Users\Kemalettin\Desktop\anlasekon\msedgedriver.exe"  # Buraya gerçek WebDriver dosya yolunu yazın
profile_path = r"C:\Users\Kemalettin\AppData\Local\Microsoft\Edge"  # Profil yolunu buraya yazın, buna gerek yok ama ben kendi hesabım ile yapsın istiyorum

# Webdriver nesnemi oluşturuyorum ve bunun üzerinden drivere ulaşarak onu çalıştıracağım service kısmına servicemi ve options kısmına default opt.larımı verdim
service = Service(executable_path=driver_path)
driver = webdriver.Edge(service=service,options = options)


# Ulaşmak istediğim ana url mi ham string olarak tanımlıyorum. Kaçış karakterlerine takılmamak için
url = r"https://www.dr.com.tr/"
# herşeyim hazır artık ulaşabilirim

driver.get(url) # siteyi açtım 
driver.maximize_window()
time.sleep(1)

# istersem direkt olarak felsefe kitaplarının xpathını verebilirim ama örnek olsun diye adım adım gideceğim 
# düz düşüneceğiz yani kendimiz yapıyormuşuz gibi kitapın üstüne geldim menü açıldı felsefe kitaplarına tıklayacağım şimdi de
# Menüde 'Kitap' öğesinin üzerine gelmek için
kitap = driver.find_element(By.XPATH,"/html/body/div[1]/header/div[3]/div[2]/ul/li[1]/a")
kitap.click()

#felsefeKitap = driver.find_element(By.XPATH,"/html/body/div[1]/header/div[3]/div[2]/ul/li[1]/div/div/div[1]/ul/li[10]/a")
#felsefeKitap.click()

try:
    # Timeout'u 20 saniyeye çıkaralım
    felsefeKitap = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div[1]/div[2]/div[1]/div/div[2]/div/div[3]/ul/li[10]/h2/a"))
    )
    felsefeKitap.click()
except Exception(TimeoutError) as ex:
    print("Öğe bulunamadı veya sayfa çok yavaş yüklendi.")

# tamam inceledim felsefe kitabı kısmı bir tablo şeklinde oraya konulmuş sıralı şekilde bir xpath a sahip olmalı inceleyelim hatta
'''
/html/body/div[1]/div[2]/div[1]/div/main/div[4]/div[1]/div/div[3]/div[1]/div[2]/h3[1]/a - kitap
/html/body/div[1]/div[2]/div[1]/div/main/div[4]/div[1]/div/div[3]/div[1]/div[2]/h3[2]/a - yazar

/html/body/div[1]/div[2]/div[1]/div/main/div[4]/div[2]/div/div[3]/div[1]/div[2]/h3[1]/a - kitap
/html/body/div[1]/div[2]/div[1]/div/main/div[4]/div[2]/div/div[3]/div[1]/div[2]/h3[2]/a - yazar
                                              kitaplarda                         yanal olarak yazarlarda bu altına yazdığım yerler değişiyor
                                                                                 yani bunları çekersem bitiyor. 
'''
for i in range(1,11):
    kitap = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/main/div[4]/div[{i}]/div/div[3]/div[1]/div[2]/h3[1]/a").text
    yazar = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/main/div[4]/div[{i}]/div/div[3]/div[1]/div[2]/h3[2]/a").text

    print(f"Felsfe kitapları bölümünde D&R sayfasının ilk 10 kitap ve yazarı:\n{kitap} : {yazar}")

time.sleep(1)# görmek için ekliyorum bunları 
driver.close()# ve driverimi kapatıyorum artık 

