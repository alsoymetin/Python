import random
bas = 1
son = 100
hak = 5
tutulan = random.randint(bas,son)
print (f"Ben {bas} ile {son} arası bir sayı tuttum")
print (f"{hak} hakkın var.")
print(tutulan)

for xx in range(hak):
    tahmin = int(input("tahminin nedir?"))
    if tahmin == tutulan:
        print("Bildin")
        break
    elif tahmin > tutulan:
        print("Tahminin olması gerekenden büyük")
        tahmin = int(input("Tahmninin nedir?"))
    elif tahmin < tutulan:
        print("Tahminin olması gerekenden küçük ")
        tahmin = int(input("Tahminin nedir?"))