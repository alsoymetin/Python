# yazarken stringe cevirme
ad = input("Kaydedilecek kisi adi: ")
no = input("Kaydedilecek kisi numarasi: ")
ogrenci={
    "Adi" : ad ,
    "Numarasi" : no
}

dosya = open("deneme2.txt","a")
dosya.write(str(ogrenci))
dosya.close()

okunan = open("deneme2.txt")
aa = okunan.read()
print(aa)
okunan.close()

