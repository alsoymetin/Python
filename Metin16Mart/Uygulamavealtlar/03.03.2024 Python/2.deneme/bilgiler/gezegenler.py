def gmenu():
    print("╔════════════════════════════════╗")
    print("║     GEZEGEN LİSTESİ            ║")
    print("║                                ║")
    print("║  1-MERKÜR                      ║")
    print("║  2-VENÜS                       ║")
    print("║  3-DÜNYA                       ║")
    print("║  4-MARS                        ║")
    print("║  5-JÜPİTER                     ║")
    print("║  6-SATÜRN                      ║")
    print("║  7-URANUS                      ║")    
    print("║  8-NEPTUN                      ║")
    print("║  9-ANAMENU                     ║")
    print("║    Seçiminiz nedir?            ║")
    print("╚════════════════════════════════╝")
    secim = input()
    if secim == "1":
        print("Merkür (0,4 AB) Güneş'e en yakın ve en küçük (0,055 Dünya kütlesi) gezegendir. Doğal uydusu yoktur ve gök taşı kraterlerinden başka bilinen tek jeolojik özelliği; büyük bir olasılıkla oluşumunun başlarında geçirdiği büzülme döneminde oluşmuş olan 'kırışıklık sırtları'dır. Merkür'ün önemsenmeyecek kadar az olan atmosferi Güneş rüzgârı nedeniyle yüzeyinden kopan atomlardan oluşur.Görece büyük demir çekirdeği ve ince mantosu henüz tam olarak açıklanamamıştır. Varsayımlar arasında, büyük bir çarpışma nedeniyle dış katmanlarından kurtulduğu ve genç Güneş'in enerjisi yüzünden tam olarak kaynaşma yoluyla büyüyemediği vardır.")
    if secim == "2":
        print("Venüs (0,7 AB) boyut olarak Dünya'ya yakındır (0,815 Dünya kütlesi) ve Dünya'ya benzer şekilde demir çekirdeğin çevresinde kalın silikat bir mantosu, önemli ölçüde bir atmosferi vardır, ayrıca iç jeolojik etkinliğin varlığına dair kanıtlar mevcuttur. Ancak Dünya'dan çok daha kurudur ve atmosferi doksan kat daha yoğundur. Venüs'ün doğal uydusu yoktur. Yüzey sıcaklığı 400 °C'nin üzerindedir, muhtemelen atmosferdeki sera gazları miktarının sebep olduğu bu durum Venüs'ü en sıcak gezegen yapar.Günümüzde jeolojik etkinlik olduğuna dair kesin kanıtlar bulunmamakla birlikte, Venüs'ün önemli ölçüde bir atmosferi oluşturacak manyetik alanı olmamasından dolayı, var olan atmosferin ancak volkanik patlamalarla yenilendiği sanılmaktadır.")
    if secim == "3":
        print("Dünya (1 AB) iç gezegenlerin içinde en büyük ve en yoğun olandır. Jeolojik etkinliği devam ettiği ve üzerinde yaşam olduğu bilinen tek gezegendir. Sıvı suküresi (hidrosfer) Yer benzeri gezegenler arasında eşsizdir ve levha hareketlerinin gözlemlendiği tek gezegendir. Dünya'nın atmosferi diğer gezegenlerin atmosferlerinden tamamen farklıdır, yaşamın olması nedeniyle %21 serbest oksijen içerecek şekilde değişmiştir. Güneş Sistemi içindeki Yer benzeri gezegenler arasında tek büyük doğal uyduya, Ay'a sahip olan gezegendir.")
    if secim == "4":
        print("Mars (1,5 AB) Dünya ve Venüs'ten küçüktür (0,107 Dünya kütlesi). Çoğunlukla karbon dioksitten oluşan önemli bir atmosferi vardır. Olympus Mons gibi yanardağlar ve Valles Marineris gibi yarık vadilerle kaplı olan yüzeyi çok yakın zamanlara kadar jeolojik etkinliğin devam ettiğini göstermektedir. Mars'ın iki çok küçük doğal uydusu vardır. Deimos ve Phobos'un Mars'ın çekimine kapılmış olan asteroitler olduğu düşünülmektedir.")
    if secim == "5":
        print("Jüpiter (5,2 AB), diğer gezegenlerin tüm kütlesinin 2,5 katına denk gelen 318 Dünya kütlesiyle en büyük gezegendir. Asıl olarak hidrojen ve helyumdan oluşmuştur. Jüpiter'in kuvvetli iç ısısı atmosferinde bulut kuşakları ve Büyük Kırmızı Leke gibi yarı kalıcı oluşumlara neden olur. Jüpiter'in bilinen altmış üç doğal uydusu vardır. En büyük dört uydusu Ganymede, Callisto, İo, ve Europa yanardağ oluşumu ile içeriden ısınma gibi özellikler bakımından Yer benzeri gezegenler ile benzerlikler gösterir.Güneş Sistemi'nin en büyük doğal uydusu Ganymede Merkür'den daha büyüktür.")
    if secim == "6":
        print("Satürn (9,5 AB), geniş halkaları ile tanınır ve atmosferik içeriği gibi çeşitli noktalarda Jüpiter ile benzerlik gösterir. Satürn'ün kütlesi çok daha azdır (95 Dünya kütlesi). Satürn'ün altmış bilinen ve üç tane doğrulanmamış doğal uydusu vardır. Bunların ikisi Titan ve Enceladus buzdan oluşmalarına rağmen volkanik etkinlik gösterir. Titan, Merkür'den daha büyüktür ve Güneş Sistemi'nde önemli bir atmosfere sahip olan tek uydudur.")
    if secim == "7":
        print("Uranüs (19,6 AB), dış gezegenlerin en hafifidir (14 Dünya kütlesi). Gezegenler arasında tutulum çemberi ile doksan derecenin üzerinde açı yapan eksenel eğikliğe sahip tek gezegendir, Güneş'in etrafında yan yatmış olarak döner. Çekirdeği diğer gaz devlerine göre daha soğuktur ve uzaya çok az ısı yayar. Uranüs'ün yirmi yedi bilinen doğal uydusu vardır. Bunlar arasında en büyükleri Titania, Oberon, Umbriel, Ariel ve Miranda'dır.")
    if secim == "8":
        print("Neptün (30 AB), Uranüs'ten biraz küçük olmasına rağmen daha ağır (17 Dünya kütlesi) ve yoğundur. Daha fazla iç ısı yaymasına rağmen bu Jüpiter ve Satürn'den daha azdır. Neptün'ün bilinen on üç doğal uydusu vardır. En büyüğü Triton sıvı nitrojenden kaynaçları ile jeolojik olarak etkindir. Triton, geri devimli yörüngeye sahip olduğu bilinen tek doğal uydudur.")
    