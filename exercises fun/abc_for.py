import pyautogui as gui
import time
import random, string

number = input('Enter the number: ')

time.sleep(5)

for i in range(int(number)):
    text = string.ascii_letters
    message = ''.join(random.sample(text, 10))
    gui.typewrite(message)
    gui.press('Enter')