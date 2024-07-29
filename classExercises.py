class Çalışan():
    personel = []

    def __init__(self,isim):
        self.isim = isim
        self.kabiliyetleri=[]
        self.personelEkle()
    
    @classmethod
    def personelSayısınıGörüntüle(cls):
        print("Şuan da {} adet personel bulunmaktadır.".format(len(cls.personel)))
    
    def personelEkle(self):
        self.personel.append(self.isim)
        print("{} adlı kişi personele eklenmiştir. ".format(self.isim))

    def kabiliyetleriGörüntüle(self):
        print("Bu kişinin kabiliyetleri: ")
        for i in self.kabiliyetleri:
            print(i)
    def kabiliyetEkle(self,kabiliyet):
        self.kabiliyetleri.append(kabiliyet)
    

'''
Burada @classmethod decoratorunu ile ilgili bir örnek yaptım. Sınıfın dışında bırakmak istemediğimiz sınıf fonksiyonlarını böylece içeride 
tanımlayabiliriz. 
'''
###########################################################################

'''
Sınıf metotları içinde bir sınıf niteliğine erişmek için ise cls kelimesinis
kullanıyoruz. İşte eğer bir sınıf içindeki herhangi bir fonksiyonda örnek veya sınıf niteliklerinin
hiçbirine erişmeniz gerekmiyorsa, statik metotları kullanabilirsiniz.

'''
# Küçük bir örnekle görelim
class Sınıf():
    sınıf_niteliği = 0
    def __init__(self,veri):
        self.veri = veri
    def veriyiGörüntüle(self):
        return self.veri
    
    @classmethod
    def sınıfMetodu(cls):
        return cls.sınıf_niteliği

    # İşte tam bu noktada hem örnek niteliklerini hem de sınıf niteliklerini kullanmayacak bir işlev yazacaksak orada @staticmethod benzeyicisi
    # statik metod oluşturabiliriz. 
    @staticmethod
    def selamla():
        print("Ben adı statik olan yaşlı bir elf'im Sizden 1000 yıl önce burada idim yine olacağım....")

'''
 Statik metotların özellikle sınıf adları üzerinden kullanılabilmesi, bu tür metotları epey
 kullanışlı hale getirir. Böylece sınıfı örneklemek zorunda kalmadan, sınıf içindeki statik
 metotlara ulaşabiliriz.

 yukarıdakini mesela Sınıf.selamla() diyerek yazdırabiliriz

'''

#Sınıf.selamla()

import time
import random
import sys

class Oyuncu():
    def __init__(self, isim, can=5, enerji=100):
        self.isim = isim
        self.darbe = 0
        self.can = can
        self.enerji = enerji
    def mevcut_durumu_görüntüle(self):
        print('darbe: ', self.darbe)
        print('can: ', self.can)
        print('enerji: ', self.enerji)
    def saldır(self, rakip):
        print('Bir saldırı gerçekleştirdiniz.')
        print('Saldırı sürüyor. Bekleyiniz.')
        for i in range(10):
            time.sleep(.3)
            print('.', end='', flush=True)
        
        sonuç = self.saldırı_sonucunu_hesapla()

        if sonuç == 0:
            print('\nSONUÇ: kazanan taraf yok')
        if sonuç == 1:
            print('\nSONUÇ: rakibinizi darbelediniz')
            self.darbele(rakip)
        if sonuç == 2:
            print('\nSONUÇ: rakibinizden darbe aldınız')
            rakip.darbele(self)
    def saldırı_sonucunu_hesapla(self):
        return random.randint(0, 2)

    def kaç(self):
        print('Kaçılıyor...')
        for i in range(10):
            time.sleep(.3)
            print('\n', flush=True)
        print('Rakibiniz sizi yakaladı')
    def darbele(self, darbelenen):
        darbelenen.darbe += 1
        darbelenen.enerji-= 1
        if (darbelenen.darbe % 5) == 0:
            darbelenen.can-= 1
        if darbelenen.can < 1:
            darbelenen.enerji = 0
            print('Oyunu {} kazandı!'.format(self.isim))
            self.oyundan_çık()
    def oyundan_çık(self):
        print('Çıkılıyor...')
        sys.exit()
##################################
# Oyuncular
siz = Oyuncu('Ahmet')
rakip = Oyuncu('Mehmet')
# Oyun başlangıcı
while True:
    print('Şu anda rakibinizle karşı karşıyasınız.',
    'Yapmak istediğiniz hamle: ',
    'Saldır: s',
    'Kaç: k',
    'Çık: q', sep='\n')
    hamle = input('\n> ')
    if hamle == 's':
        siz.saldır(rakip)
        print('Rakibinizin durumu')
        rakip.mevcut_durumu_görüntüle()
        print('Sizin durumunuz')
        siz.mevcut_durumu_görüntüle()
    if hamle == 'k':
        siz.kaç()
    if hamle == 'q':
        siz.oyundan_çık()