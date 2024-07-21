# if else yapısı zaten bildiğimiz bir şey dinleyip bir örnek göstereceğiz o kadar syntax ı görmek açısından
x = 5
if x==5:
    print("X in değeri 5 e eşittir", x)
else: 
    print("X in değeri 5 e eşittir")
'''
ELİF YAPISI
# ara koşullar için ise elif yapısı vardır 
kullanıcıAdı = "Kemal"
kullanıcıŞifresi = "1234"

if kullanıcıAdı == "Kemal" and kullanıcıŞifresi == "1234":
    print("Giriş başarılı")
elif kullanıcıAdı != "Kemal":
    print("Kullanıcı adı hatalı")
elif kullanıcıŞifresi != "1234":
    print("Şifre yanlış")
else:
    print("Giriş bilgileri yanlış")

# if else kullanarak basit bir hesap makinesi yapma örneği
sayı1 = 0
sayı2 = 0
operat = input("Hesap makinesi açıldı lütfen yapmak istediğiniz işlemin operatörünü giriniz\n Toplama : +\n Çıkartma: -\n Çarpma: *\n Bölme: / ")
if (operat == "+") :
    print("Toplamak istediğiniz iki sayıyı giriniz")
    sayı1 = int(input("1.Sayıyı giriniz"))
    sayı2 = int(input("2.Sayıyı giriniz"))
    print("Sonuç: ", (sayı1 + sayı2) )
elif (operat == "-") :
    print("Çıkartmak istediğiniz iki sayıyı giriniz")
    sayı1 = int(input("1.Sayıyı giriniz"))
    sayı2 = int(input("2.Sayıyı giriniz"))
    print("Sonuç: ", (sayı1 - sayı2) )
elif (operat == "-") :
    print("Çıkartmak istediğiniz iki sayıyı giriniz")
    sayı1 = int(input("1.Sayıyı giriniz"))
    sayı2 = int(input("2.Sayıyı giriniz"))
    print("Sonuç: ", (sayı1 - sayı2) )    
elif (operat == "*") :
    print("Çarpmak istediğiniz iki sayıyı giriniz")
    sayı1 = int(input("1.Sayıyı giriniz"))
    sayı2 = int(input("2.Sayıyı giriniz"))
    print("Sonuç: ", (sayı1 * sayı2) )
elif (operat == "/") :
    print("Bölmek istediğiniz iki sayıyı giriniz")
    sayı1 = int(input("1.Sayıyı giriniz"))
    sayı2 = int(input("2.Sayıyı giriniz"))
    print("Sonuç: ", (sayı1 / sayı2) )
else: 
    print("Yanlış operatör seçtiniz !!!")'''

# For döngüleri
x = [1,2,3,4,5,56,"Kemalettin"]
for i in x:
    print(i)

# c++ daki range based for döngüleri gibi çalışırılar 
# C++ daki gibi nasıl kullanırız dersen burada range() fonksiyonu devreye giriyor

sayı = range(0,101,3) #3 parametre alır opsiyonel tabi başlangıç bitiş adım şeklinde
for i in sayı:
    print(i)

# while döngüsü
# çalışma şekli while koşul: sonra alt satıra indentli bir şekilde kodları koyarız ve koşul sağlandığı sürece çalışır

# while true:     sonsuz döngü oluşturmak için bu şekilde de kullanılanilir 
sayı = 0 
while sayı <30: 
    print(sayı)
    sayı += 1


# döngüleri kontrol etmek içni kullanılan break ve continue ifadeleri tüm dillerde aynı olduğu için atladım 
# Sayı tahmin oyunu 
print("Toplam 3 hakkınız vardır\n Tahmin edilecek sayı 0-100 arasındadır.\n")
hak = 3
sayı = 54
while True:
    tahmin = int(input("Başlamak için bir sayı giriniz Çıkış için [Q] basınız"))
    if tahmin == sayı:
        buldu = input("Tebrikler doğru tahmin ettiniz, tekrar oynamak için [T] çıkmak için [Q] basınız")
        if buldu == "Q":
            break
        else:
            hak = 3
            continue
    else:
        hak -= 1
        print(f"Yanlış tahmin {hak} hakkınız kaldı")
        if hak == 0:
            break
        
#kaçış dizileri c++ deki gibi o yüzden tekrar ederken bakarsın izledik geçtik