import hesaplar.hesaplamalar
def hmmenu():
    print("╔═════════════════════╗")
    print("║HESAP MAKİNESİ       ║")
    print("║                     ║")
    print("║  1-Toplama          ║")
    print("║  2-Çıkarma          ║")
    print("║  3-                 ║")
    print("║  4-                 ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input ()

    if secim == "1" :
        hesaplar.hesaplamalar.toplamamenu ()
        hmmenu ()
