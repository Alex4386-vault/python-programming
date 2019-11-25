import p as tur
import math

t = tur.Pen()
scr = tur.Screen()

t.penup()
t.backward(450)
t.pendown()

t.circle(100, 180)
t.right(90)
t.backward(200)

t.penup()
t.right(90)
t.forward(125)
t.pendown()

for i in range(3):
    t.forward(125)
    t.left(120)

t.penup()
t.forward(200)

t.pendown()
t.left(90)
t.forward(125)
t.right(150)
t.forward(125*2/math.sqrt(3))
t.left(150)
t.forward(125)
t.backward(125)

t.right(90)

t.penup()
t.forward(20)
t.pendown()

for i in range(3):
    t.forward(125)
    t.left(120)
    
t.penup()
t.forward(140)

t.pendown()
t.left(90)
t.forward(125)
t.backward(125)
t.right(90)
t.forward(70)

while True:
    print("done")







