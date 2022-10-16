import turtle
import random

t = turtle.Turtle()

# t.penup() - żółw nie rysuje
# t.pendown() - żółw rysuje

for i in range(16):
    #t.width(i + 1)
    # t.color( random.choice(['red','orange','blue','green']))
    if i <= 7:
        t.color('red')
        t.forward(100)
        t.right(45)
        t.fd(50)
        t.left(90)
        t.bk(50)
        t.goto(0,0)
    if i > 7:
        t.color('blue')
        t.forward(120)
        t.right(45)
        t.fd(50)
        t.left(90)
        t.bk(62)
        t.goto(0,0)
    

turtle.mainloop()


