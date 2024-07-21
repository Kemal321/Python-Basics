#print(2+2)

x = 1 # int tam sayılar olarak geçiyor 
print(type(x)) # her hangi bir şeyin tipini sorgulamak istediğimizde type fonksiyonu nu kullanıyoruz 

c = 2+3j # Diğer dillere nazaran python da aynı zaman da complex dediğimiz karmaşık sayılar da bir veri tipi olarak vardır 

print(type(c))

print(c.real,'\n',c.imag ) # burada da real ve imag fonksiyonları ile complex sayıların sanal ve gerçek kısmını da yazdırabiliriz 

#################################Ders 10 - Sayısal veri tipleri bitti bu kadardı evet #################################################

# Tabi ki bir çok built in fonksiyonlar var onları da zamanla görerek kullanarak da göreceğiz. Python için istihzaya da bakabilirsin.

xx = "Kemalettin KARA boş tekrar atıyor. "

print(type(xx)) 

#python da string dediğimiz metinsel ifadelerde indeksleme vardır indeksler amerikan standardı olduğu için 0 dan başlar.

print(xx[0])  # mesela 0.indeks yani başlangıç indeksini K olarak dönecektir. Unutmayın boşlukta bir karakterdir. 

print(xx[-4])  # evet indekslerde eksi indekste var. Eksi indeks ise sondan başlayarak eksi yönde sayacaktır.

##Bir aralıkta indek istediğimiz de matlab daki gibi kullanımı var mesela 
print(xx[0:11]) # burada mesela direktmen benim ismimi yazdırdı böylece bir aralığı aldık zaten Matlab Python ve C++ ın bir karışımı olarak düşünürsek aslında matlab da 
                # var olan aralığı adım adım bölme veya aralıklı sayı üretme gibi bir çok built in fonksiyon da burada mevcut zaten zamanla göreceğiz onları da

print(xx[0:11:2]) # burada atlayarak seçme için tekrar çift noktayı kullanarak step= diye yukarıuda açıklama çıkar zaten bu şekilde atlayarak indeksleme yaparız


# Burada sayısal verilerde 4 işlem olduğu gibi metinsel ifadelerde de 4 ilem vardır bunlar şu şekilde çalışır 
ornekMetin = "Örnek" 

print(ornekMetin + ornekMetin)  # burada görüleceği üzere toplama ifadesi direktmen birleştirme için kullanılır. matlab da ise bunun karşılığı concatination gibi bir şey concat() 
                                # fonksiyonuydu sanırım 
print(ornekMetin * 2 )  #Bu örnekten göreceğin üzere çarp işlemi de mantıksal olarak sayı kadar tekrarlama anlamına gelir mesela "ÖrnekÖrnek" olarak çıktı verecek
                        # Python case sensitive bir dildir. Yani büyük ve küçük harf hassasiyeti vardır kemal ile Kemal veya KEmal aynı şey değildir. 
                        # Metinlerde bölme ve çıkarma işlemi yoktur. 

# kullandığımız metinsel ifadenin uzunluğu ne kadar dersek yine klasik len() fonksiyonunu kullanırız. C++ de length()

# Boolean değerlerini not almicam C++ de de diğer dillerde de çoğunlukla aynı zaten. 
