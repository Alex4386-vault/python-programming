import turtle
import time

scr = turtle.Screen()
scr.bgcolor("skyblue")

global_speed = 0

def triangle(x1, y1, width):
    p = turtle.Pen()
    p.speed(global_speed)
    height = (width*(3**1/2))/2
    p.penup()
    p.goto(x1,y1)
    p.setheading(270)
    p.forward(height)
    p.pendown()
    p.left(90)
    p.forward(width)
    p.left(120)
    p.forward(width)
    p.left(120)
    p.forward(width)
    p.hideturtle()
    del p

def filltriangle(x1, y1, width, color):
    p = turtle.Pen()
    p.speed(global_speed)    
    p.penup()
    p.fillcolor(color)
    height = (width*(3**1/2))/2
    p.goto(x1,y1)
    p.setheading(270)
    p.forward(height)
    p.pendown()
    p.begin_fill()
    p.left(90)
    p.forward(width)
    p.left(120)
    p.forward(width)
    p.left(120)
    p.forward(width)
    p.end_fill()
    p.hideturtle()
    del p    

def rectangle(x1, y1, width):
    p = turtle.Pen()
    p.speed(global_speed)
    p.penup()
    p.goto(x1,y1)
    p.pendown()
    for i in range(4):
        p.forward(width)
        p.right(90)
    p.hideturtle()
    del p

def fillrectangle(x1, y1, width, color):
    p = turtle.Pen()
    p.speed(global_speed)
    p.penup()
    p.fillcolor(color)
    p.goto(x1,y1)
    p.pendown()
    p.begin_fill()
    for i in range(4):
        p.forward(width)
        p.right(90)
    p.end_fill()
    p.hideturtle()
    del p

def circle(x1,y1,radius):
    p = turtle.Pen()
    p.speed(global_speed)
    p.penup()
    p.goto(x1,y1)
    p.pendown()
    p.forward(radius/2)
    p.circle(radius,-360)
    p.hideturtle()
    del p

def fillcircle(x1,y1,radius,color):
    p = turtle.Pen()
    p.speed(global_speed)
    p.penup()
    p.goto(x1,y1)
    p.pendown()
    p.forward(radius/2)
    p.fillcolor(color)
    p.begin_fill()
    p.circle(radius,-360)
    p.end_fill()
    p.hideturtle()
    del p

p = turtle.Pen()
p.speed(global_speed)
filltriangle(-400,200,200,"pink")
fillrectangle(-400,50,200,"blue")
p.penup()
p.goto(-300,73.5+(200*(3**1/2))/2)
p.backward(100)
p.write("House",font=("Arial",20))
p.forward(100)
p.fillcolor("orange")
p.pendown()
p.begin_fill()

how_far = 200
tilt = 30
p.left(tilt)
p.forward(how_far)
p.right(90)
p.forward(200)
p.right(90)
p.forward(how_far)
p.right(90)
p.forward(200)
p.end_fill()
p.fillcolor("yellow")
p.begin_fill()
p.backward(200)
p.right(tilt)
p.backward(200)
p.right(90-tilt)
p.forward(how_far)
p.left(90-tilt)
p.forward(200)
p.left(90+tilt)
p.forward(how_far)
p.end_fill()
p.hideturtle()

fillrectangle(-350,-50,100,"green")

p.showturtle()
p.penup()
p.goto(-200,50)
p.left(90-tilt)
p.forward(100)
p.left(90+tilt)
p.forward(how_far*0.6)
p.tilt(90-tilt)
p.fillcolor("brown")
p.begin_fill()
p.pendown()
p.forward(50)
p.left(90-tilt)
p.forward(50)
p.left(90+tilt)
p.forward(50)
p.left(90-tilt)
p.forward(50)
p.end_fill()
p.penup()
p.hideturtle()

p.goto(200,-100)
p.setheading(0)
p.showturtle()
p.fillcolor("brown")
p.begin_fill()
p.pendown()

p.forward(50)
p.right(90)
p.forward(100)
p.right(90)
p.penup()
p.backward(50)
p.write("Tree",font=("Arial",20))
p.forward(50)
p.pendown()

p.forward(50)
p.right(90)
p.forward(100)
p.right(90)

p.penup()
p.end_fill()


p.forward(25)
p.forward((3**(1/2)*75))


for i in range(3):
    p.pendown()
    p.fillcolor("green")
    p.begin_fill()
    p.left(150)
    p.forward(150)
    p.left(60)
    p.forward(150)
    p.left(150)
    p.forward(3**(1/2)*150)
    p.end_fill()
    p.penup()
    p.left(90)
    p.forward(75)
    p.right(90)



p.setheading(0)

p.goto(100,250)
p.setheading(0)

p.fillcolor("yellow")
p.pendown()
p.begin_fill()

stroke = 50
for i in range(8):
    p.circle(50,-45)
    p.right(90)
    p.forward((stroke / 2) + ((i % 2) * (stroke / 2)))
    if i == 5:
        p.penup()
        p.forward(50)
        p.write("Sun",font=("Arial",20))
        p.backward(50)
        p.pendown()
    p.backward((stroke / 2) + ((i % 2) * (stroke / 2)))
    p.left(90)

    

p.end_fill()

del p


p = turtle.Pen()
p.hideturtle()
p.setheading(90)
p.penup()
p.shape("turtle")
p.goto(-300,-200)
p.fillcolor("black")
p.showturtle()
