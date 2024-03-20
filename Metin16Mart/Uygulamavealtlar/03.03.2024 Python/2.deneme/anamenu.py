import hesaplar.hesapmakinesi
import hizhesap.hizhesapuyg
import nothesap.nothesaplama
import cizimler.cizim
import hesaplar.sicaklik
import bilgiler.gezegenler
def anamenu():
    print("╔════════════════════════════════╗")
    print("║     ANAMENU                    ║")
    print("║                                ║")
    print("║  1-Hesap Makinesi              ║")
    print("║  2-KMH'den MPH dönüştürücü     ║")
    print("║  3-Harf Notu Hesaplama         ║")
    print("║  4-Şekil Çizimi                ║")
    print("║  5-Sıcaklık Dönüştürücü        ║")
    print("║  6-Gezegenler hakkında bilgiler║")
    print("║  e-Çıkış                       ║")    
    print("║                                ║")
    print("║    Seçiminiz nedir?            ║")
    print("╚════════════════════════════════╝")
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
    if secim == "4" :
        cizimler.cizim.cmenu ()
        anamenu ()
    if secim == "5" :
        hesaplar.sicaklik.smenu ()
        anamenu ()
    if secim == "6" :
        bilgiler.gezegenler.gmenu ()
        anamenu ()   
    if secim == "E" or secim == "e" :
        exit ()
    else:
        print ("secim sadece 1,2,3,4,e olabilir.")
        anamenu ()

anamenu ()

    
