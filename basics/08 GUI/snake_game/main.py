import turtle
import time
from food import *
from snake import *

win = turtle.Screen()
win.title('Snake Game')
width = 500
height = 500
win.setup(width=width, height=height)
win.bgcolor('green')

snake = Snake(0,0)
win.listen()
win.onkey(snake.key_up, 'Up')
win.onkey(snake.key_down, 'Down')
win.onkey(snake.key_left, 'Left')
win.onkey(snake.key_right, 'Right')


food = Food()

while True:
    win.update() # odświeżenie ekranu (odrysowanie go)
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
    
    if snake.check_self_collision() or snake.check_walls_collision(width, height):
        food.refresh
        snake.refresh()

win.mainloop()
