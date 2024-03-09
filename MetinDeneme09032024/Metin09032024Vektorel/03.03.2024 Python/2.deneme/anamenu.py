import hesaplar.hesapmakinesi
import hizhesap.hizhesapuyg
import nothesap.nothesaplama
def anamenu():
    print("╔═════════════════════╗")
    print("║     ANAMENU         ║")
    print("║                     ║")
    print("║  1-hesap mak        ║")
    print("║  2-kmh hesap        ║")
    print("║  3-not hesaplaması  ║")
    print("║  4-cizim            ║")
    print("║  5-                 ║")
    print("║  e-cikis            ║")    
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input ()
    if secim == "1" :
        hesaplar.hesapmakinesi.hmmenu ()
        anamenu ()
    if secim == "2" :
        hizhesap.hizhesapuyg.hizmenu ()
        anamenu ()
    if secim == "3" :
        nothesap.nothesaplama.notmenu ()
        anamenu ()
    if secim == "E" or secim == "e" :
        exit ()
    else:
        print ("secim sadece 1,2,3,4,e olabilir.")
        anamenu ()

anamenu ()

    
