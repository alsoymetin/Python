import turtle
def kare():
    for a in range(4):
        turtle.forward(100)
        turtle.right(90)

def ucgen():
    for abc in range(3):
        turtle.forward(100)
        turtle.right(120)  

def altigen(rnk):
    turtle.color(rnk)
    for abc in range(6):
        turtle.forward(100)
        turtle.right(60)   

def cmenu():

    print("╔═════════════════════╗")
    print("║CIZIMLER             ║")
    print("║                     ║")
    print("║  1-Kare Ciz         ║")
    print("║  2-Ucgen Ciz        ║")
    print("║  3-Altigen Ciz      ║")
    print("║  4-                 ║")
    print("║                     ║")
    print("║    Seçiminiz nedir? ║")
    print("╚═════════════════════╝")
    secim = input ()

    if secim =="1" : kare()
    if secim =="2" : ucgen()
    if secim =="3" : altigen()
        

