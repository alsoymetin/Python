import hesaplar.hesapmakinesi
import hizhesap.hizhesapuyg
def anamenu():
    print("╔═════════════════════╗")
    print("║     ANAMENU         ║")
    print("║                     ║")
    print("║  1-hesap mak        ║")
    print("║  2-kmh hesap        ║")
    print("║  3-geri don         ║")
    print("║  4-                 ║")
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
        
anamenu ()

    
