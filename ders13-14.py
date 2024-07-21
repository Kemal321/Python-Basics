# Veri tipi değiştirme burada direkt değiştirme yapıyoruz adını tam hatırlamadım ama öyle diyelim
# yani veritipi(değiştirilecekobje) örneklerle gösterelim 
a = 2 
b= str(a)
print(type(a))  # sonucunda göreceksiniz b artık bir string 
# listeden tupleye stringden integer e integerden stringe bir çok değişim yapılabilir. 


########################################################################################################################################

# kullanıcıdan veri alma input() fonksiyonu

x = int(input("Bir sayı giriniz: ")) # burada bilmen gereken şey aynı c++ std::cin de olduğu gibi girilen veri string olarak alınır 
y = int(input("Bir sayı daha gir toplayak: "))
print(x + y)

#######################################################
# Dairenin alanı
çap = float(input("Bir sayı daha gir toplayak: "))
alan = 3*çap*çap
print("Dairenin alanı :",alan)