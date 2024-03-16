def topla (aa,bb=0):
    return aa+bb

def carp(x,y):
    return x*y

sayi1 = 10
sayi2 = 7

print (topla(sayi1))
print (topla(sayi1,sayi2))
print (f"Toplam sonuc:{topla(sayi1,sayi2)}")
print (topla(sayi1,topla(8,sayi1)))
print (carp(sayi1,sayi2))
