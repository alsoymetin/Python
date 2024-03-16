import turtle
import random
renkler= ["red", "blue", "magenta", "yellow", "pink", "green", "black", "cyan", "orange"]
for a in range(4):
    #print(renkler[a])
    #turtle.color(renkler[a]) -sırayla yazdırır
    turtle.color(random.choice(renkler))
    turtle.forward(100)
    turtle.right(90)

input()