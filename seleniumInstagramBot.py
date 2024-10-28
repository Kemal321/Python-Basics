from seleniumInstagranBotUserInfo import kullaniciAdi, sifre
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.chrome.service import Service


# Driverime ulaşmam gerek o yüzden path yollarını hazır ettim. Edge WebDriver'ın dizin yolu
#driver_path = r"C:\Users\Kemalettin\Desktop\anlasekon\msedgedriver.exe"  # Buraya gerçek WebDriver dosya yolunu yazın
#profile_path = r"C:\Users\Kemalettin\AppData\Local\Microsoft\Edge"  # Profil yolunu buraya yazın, buna gerek yok ama ben kendi hesabım ile yapsın istiyorum
#service = Service(executable_path=driver_path)

#driver = webdriver.Edge(service=service)

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=selenium") 
service = Service(executable_path= r"C:\Users\Kemalettin\Desktop\anlasekon\Python\chrome.exe" )
driver = webdriver.Chrome()
url="https://www.instagram.com/"

driver.get(url)

ka = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
ka.send_keys(kullaniciAdi)

sf=driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
sf.send_keys(sifre)
sf.send_keys(Keys.ENTER)
time.sleep(2)
driver.maximize_window()
time.sleep(30000)

driver.close()

'''
By.XPATH bile doğru olsa service ve optionslar olmayınca çalışmadı otomatik olarak aldığını düşünsem de oluşturduğum değişkenleri neye göre alıyor 
tam olarak anlamadım yani verdiğim değişkenler pasif durumda olmadıkları belli. Tam olarak neden çalışıyor anlamış değilim çok fazla Türkçe kaynak
bulunmadığı için aldığım hataları da tam olarak bulamadım. Bu şekilde giriş yapabiliyor. ama çalışması için gerekli driver ın path i yok iken bile 
çalışıyor garip bir şekilde yaptım anlamadım dümdüz bırakınca kendisi hallediyor. Hatayı aramaya devam edeceğim ama buradan ileriye doğru da devam
edeceğim yoksa bu derslerde takılıp kalacağım. Çözerseniz aşağıya yorum bırakın lütfen. :))
'''

