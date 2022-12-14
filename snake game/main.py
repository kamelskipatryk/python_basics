import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
import sys

# klasa kostka węża
class Cube(object):
    rows = 20
    def __init__(self, start, dirnx = 1, dirny = 0, color=(0, 0, 0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes = False):
        dis = size // rows
        rw = self.pos[0]
        cm = self.pos[1]
        pygame.draw.rect(surface, self.color, (rw * dis + 1, cm * dis + 1, dis - 2, dis - 2))

# klasa wąż
class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            # zamyka grę po wciśnięciu X
        
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_RIGHT]:
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_UP]:
                self.dirnx = 0
                self.dirny = -1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_DOWN]:
                self.dirnx = 0
                self.dirny = 1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body - 1):
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows -1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows -1:
                    c.pos = c(c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows -1)
                else:
                    c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

# funkcja rysowania siatki
def draw_grid(width, rows, surface):
    size_between = width // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + size_between
        y = y + size_between
        pygame.draw.line(surface, (255,255,255), (x,0), (x,width))
        pygame.draw.line(surface, (255,255,255), (0,y), (width,y))

# funkcja rysowania okna
def draw_window(surface):
    surface.fill((0, 255, 0)) # RGB
    s.draw(surface)
    draw_grid(size, rows, surface)
    pygame.display.update()

#TO DO: stwórz funkcję rysowania jabłuszka 
#TO DO: stwórz funkcję dla okna informacyjnego 

def main():
    global size, rows, s
    size = 500 # obszar gry
    rows = 20 # wiersze
    
    window = pygame.display.set_mode((size, size))

    s = Snake((0, 0, 0), (10, 10))

    clock = pygame.time.Clock()

    while True:
        pygame.event.poll()
        for event in pygame.event.get():
            # zamyka grę po wciśnięciu X
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.time.delay(50) # im mniej delay tym gra szybsza
        clock.tick(10) # im mniej tick tym gra wolniejsza

        draw_window(window)


main()