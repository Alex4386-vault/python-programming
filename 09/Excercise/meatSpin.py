import p
wa = p.Screen()
wa.bgcolor("black")

t = p.Pen()
t.speed(0)

t.shape("turtle")
t.pencolor("yellow")

radius = 100
rotate = 4
initMove = 20

colors = ['red','orange','yellow','green','blue','purple']

t.penup()
t.left(90)
t.forward(radius / 2)
t.right(90)
t.pendown()

for x in range(500):
    t.pencolor(colors[x % len(colors)])
    t.pendown()
    t.forward(initMove - ((initMove / 1000) * x))
    t.right(rotate)
    t.circle(radius)
    radius *= 0.98
    rotate *= 1.02
    t.penup()
