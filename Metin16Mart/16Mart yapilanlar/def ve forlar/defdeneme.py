def topla(aa,bb):
    return f"topla:{aa+bb}"

def carp(x,y):
    return f"carp:{x*y}"

def cikarma():
    print(f"Cikarma:{18-3}")

def bolme():
    print(f"Bolme:{18/2}")

def carpvebol():
    print(f"carpvebol:{18*2/3}")

sayi1 = int(input("Birinci Sayı nedir?"))
sayi2 = int(input("İkinci sayı nedir"))


print (carp(sayi1,sayi2))
print (topla(sayi1,sayi2))
bolme()
carpvebol()
