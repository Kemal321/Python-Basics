# köşeli parantezler içinde [veri1, veri2, ...] şeklinde saklanan bir veri tipidir en önemlisi denebilir
listem = ["Kemaleddin", "KARA", 25]
print(listem, type(listem)) 
 # Liste veri tipinde farklı türde veriler saklayabiliriz fakat C++ taki liste yani array yapılarında böyle bir durum yoktur.

## Burada da indeksleme vardır aslında stringlerde birer listedir sadece sadece metinsel charlardan oluşan listedir diyebiliriz.

stringlistesi = "Kemalettin"
print(stringlistesi[1])

print(listem[2])


# String ve listelerin en önemli farkı ise stringler immutabledır yani sabit ifadelerdir oluşturulduktan sonra değiştirilemezdir. Liste tipi ise
# sabit ifade değildir oluşturulduktan sonra değiştirilebilir bir ifade olarak saklanır aşağıda göreceksin

listem[0] = "Cemal"
print(listem[0])

# listelerin içinde başka listelerde saklanabilir, ek olarak hem len() fonksiyonu burada çalışır ve içeride bir liste daha varsa o da 1 elemandır
yeniListem = [listem, "bu yeni liste"]
print(len(yeniListem), yeniListem)

# Daha önce gördük listelerde kendi aralarında toplanabiliyor 

listem = listem + ["Şanlıurfa"] # artık şanlıurfa da eklenmiş olacak 
print(listem)

# bazen listeleri tersten çağırmamız da gerekebilir o zaman ne yapacağız yine indeksleme mantığı ile 
print(listem[::-1])  # bu listemizi tersten getirecek bize tabi mantığını kavrayalım aslında bu bir çember şeklinde olan bir masanın etrafında 
                    # size geriye doğru birer adım atarak koltuklardaki kişileri say dediğimiz bir duruma benziyor aslında yine tüm liste ama tersten
print(listem[::]) # Bu indeksleme mantığı da tüm listemizi çağırır 















