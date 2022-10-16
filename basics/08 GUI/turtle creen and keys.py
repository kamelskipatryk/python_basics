import turtle
import time

t = turtle.Turtle()
win = turtle.Screen()

win.title('Aplication')
win.bgcolor('yellow')
win.setup(width=550, height=550)

t.forward(100)
print( 'x', t.xcor() )
print( 'y', t.ycor() )

def key_pressed_w():
    print('w clicked')
    t.fd(20)

def key_pressed_s():
    print('s clicked')
    t.bk(20)

def key_pressed_d():
    print('d clicked')
    t.right(90)

def key_pressed_a():
    print('a clicked')
    t.left(90)

win.listen()
win.onkey(key_pressed_w, 'w')
win.onkey(key_pressed_s, 's')
win.onkey(key_pressed_d, 'd')
win.onkey(key_pressed_a, 'a')

win.tracer(0)

while True:
    win.update()
    time.sleep(0.1)




win.mainloop()



