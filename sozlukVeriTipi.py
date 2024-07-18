# Sözlük veri tipleri diğer dillerde çok bulunmayan bir veri tipidir C gibi dillerden bahsediyorum 
# {"key": value, ....} şeklinde tanımlanan ve indeksi olmayan bir veri tipidir çünkü zaten key veya valueden ulaştığımız bir veri tipidir

örnekSozluk = {"İsim: ": "Kemalettin", "Soyad: ": "KARA", "Yaş: ": 25, 234:"lfglf" }
print(örnekSozluk,"\n", type(örnekSozluk))

# Burada mevcut değerleri değiştirebiliriz veya yeni anahatar değer çifti ekleyebiliriz. 
örnekSozluk["Yeni değer: "] = "Ne güzel ekledik aga" # Burada yeni çift ekledik 
örnekSozluk["İsim: "] = "Ad: "  # Burada da mevcut bir değeri değiştirdik ama sadece değerleri değiştirebiliriz
print(örnekSozluk)

# Sözlükler iç içe yapıda da kullanılabilir örnekle görelim

kullanıcılar = {"Kullanıcı1": {"İsim: ": "Kemalettin", "Soyad: ": "KARA", "Yaş: ": 25 },
                "Kullanıcı2": {"İsim: ": "Cemal", "Soyad: ": "KARA", "Yaş: ": 27 }
}
print(kullanıcılar["Kullanıcı1"])
###################################################################################################################################################

# Demetler yani tuple yapıları değiştirilemeyen bir diğer yapımız. Genelde sistem konfigürasyon kodları tuple şeklinde saklanır ki değiştirilmesin
# Saklanabilir diyelim ya da bize öyle demişlerdi

# Tanımlama şekli (veri1,veri2,veri3, .....) değiştirilemez verileri saklamak için kullanılır indekslenebilir. 
örnekDemet = ("DemetOluşturduk","Dİğer veri",23,21)  # bu bir özel durumdur tuple oluşturacaksak ve tuple da tek bir eleman varsa bile elemanın sonuna virgül koymalıyız
                                  # Çünkü aksi halde bunun bir parantez içine alma işlemi mi yoksa bir demet mi ayıramayız
print(örnekDemet, type(örnekDemet))
print(örnekDemet[1])

###################################################################################################################################################
# Küme veri tipi bir diğer veri tipimiz değiştirilemez üzerinde işlem yapmak için metodları kullanırız. 
# indekslenemez yapıdadırlar, veri çekeceğimiz zaman döngülerle veri çekeriz. Tekrarlı veriye izin vermez bu en önemli özelliğidir
# Yani kümelerde Çoğul elemana izin vermeyen tiptir. Sözlükler gibi süslü parantez kullanır. Sözlüklerdeki gibi iki nokta kullanarak ayrım 
# yapmazsak bunun küme olduğu anlaşılır 

örnekKüme = {"BU bir kümedir", "Burada tekrar olmaz ","Burada tekrar olmaz ", 232,212,3} # mesela tekrar eden 2 veri var ama print ile sadece 1 tane
print(örnekKüme, type(örnekKüme))


