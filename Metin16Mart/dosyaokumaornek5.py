# try:
#     okunan = open("deneme1.txt", "r")
#     print(okunan.readline())
#     print(okunan.readline())
#     okunan.close()
# except:
#     print("Bir hata oluştu.")

# okunan = open("deneme1.txt", "r")
# a = okunan.read(5)
# b = okunan.read(6)
# print (a,b)
# okunan.close()

okunan = open("deneme1.txt", "r")
for a in okunan:
    print(a)

okunan.close()
