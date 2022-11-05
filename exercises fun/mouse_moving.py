import pyautogui as pg
import random
import time

number = 0

while True:
    x = random.randint(500,900)
    y = random.randint(100,800)
    pg.moveTo(x,y,2)
    time.sleep(0.5)
    number += 1
    if number == 10:
        break
