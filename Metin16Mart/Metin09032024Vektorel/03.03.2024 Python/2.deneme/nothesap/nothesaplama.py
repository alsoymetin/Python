def notmenu():
    print ("Bu fonksiyon harf notlarını hesaplar")
    Not = int(input("Notun Nedir"))
    if Not >100 or Not <0: print("Yanlış giriş'0-100 arası sayı giriniz'")
    else:
        if Not >= 90 : print("Notun AA")
        elif Not >= 80 : print("Notun BA")
        elif Not >= 70 : print("Notun BB")
        elif Not >= 60 : print("Notun CB")
        elif Not >= 50 : print("Notun CC")
        elif Not < 50 : print("Kaldınız")
        if Not > 70 and Not <90: print("İyi")

    
