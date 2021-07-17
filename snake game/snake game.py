#start date: 28/04/2020
#finish date: 25/05/2020

###libraries
import random
import pygame
from pygame import *
import sys
import os
import time
from tkinter import *

###objects
class snake:
        def __init__(self, win):
                self.score = 1
                self.length = 25
                self.width = 25
                self.win = win
                self.r = random.randint(0,500)
                self.vel = 25
                self.update = pygame.display.update()
                self.right = True
                self.left = False
                self.up = False
                self.down = False
                # 0 = right     1 = left        2 = up          3 = down
                self.can = [True, False, True, True]
                self.keys = pygame.key.get_pressed()

                while True:
                        if self.r % 25 == 0:
                                break
                        else:
                                self.r = random.randint(0,500)
                                continue
                self.x = self.r
                self.y = self.r
                self.body = [] # list of body elements

                self.r = random.randint(0,500)
                while True:
                        if self.r % 25 == 0:
                                break
                        else:
                                self.r = random.randint(0,500)
                                continue
                self.a = self.r
                self.b = self.r


        def move(self, win):
                win.fill((0,0,0))
                self.keys = pygame.key.get_pressed()

                # move snake
                self.body.insert(0, (self.x, self.y))

                if self.right == True:
                        self.x += self.vel
                if self.left == True:
                        self.x -= self.vel
                if self.up == True:
                        self.y -= self.vel
                if self.down == True:
                        self.y += self.vel

                if self.x > 475:
                        self.x = 0
                if self.x < 0:
                        self.x = 500
                if self.y > 475:
                        self.y = 0
                if self.y < 0:
                        self.y = 500

                # remove element at end
                while len(self.body) >= self.score:
                    del self.body[-1]

                if self.keys[pygame.K_RIGHT] and self.can[0] == True:
                        self.right = True
                        self.left= False
                        self.up = False
                        self.down = False
                        self.can[1] = False
                        self.can[0] = True
                        self.can[2] = True
                        self.can[3] = True

                if self.keys[pygame.K_LEFT] and self.can[1] == True:
                        self.right = False
                        self.left = True
                        self.up = False
                        self.down = False
                        self.can[0] = False
                        self.can[1] = True
                        self.can[2] = True
                        self.can[3] = True

                if self.keys[pygame.K_UP] and self.can[2] == True:
                        self.right = False
                        self.left = False
                        self.up = True
                        self.down = False
                        self.can[3] = False
                        self.can[0] = True
                        self.can[1] = True
                        self.can[2] = True

                if self.keys[pygame.K_DOWN] and self.can[3] == True:
                        self.right = False
                        self.left = False
                        self.up = False
                        self.down = True
                        self.can[2] = False
                        self.can[0] = True
                        self.can[1] = True
                        self.can[3] = True

                # draw smake and body
                self.snake = pygame.draw.rect(self.win, (0,255,0), (self.x, self.y, 25, self.width))
                for pos in self.body:
                    pygame.draw.rect(self.win, (0,255,0), (pos[0], pos[1], 25, self.width))
                    if self.x == pos[0] and self.y == pos[1]:
                            pygame.quit()
                            
                            sb = Tk()
                            sb.title("Score")
                            sb.geometry("100x50")
                            Label(sb, text = "SCORE:").pack()
                            Label(sb, text = self.score).pack()
                            
                            sb.mainloop()


        def food(self, win):
                pygame.draw.rect(self.win, (255,0,0), (self.a, self.b,25,25))

                if self.a == self.x and self.b == self.y:
                        self.r = random.randint(0,500)
                        while True:
                                if self.r % 25 == 0 and self.r < 500:
                                        break
                                else:
                                        self.r = random.randint(0,500)
                                        continue
                        self.a = self.r
                        self.b = self.r
                        self.score += 1

###main game	

##variables
screen = (500,500)
W = 25
L = 25
WHITE = 255,255,255
clock = pygame.time.Clock()

##game
pygame.init()
win = pygame.display.set_mode(screen)
title = pygame.display.set_caption("snake game")
update = pygame.display.update()
snake = snake(win)

run = True
while run:
        clock.tick(10)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
        snake.move(win)
        snake.food(win)
        pygame.display.update()

pygame.quit()
