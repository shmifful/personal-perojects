import pygame
from pygame.constants import MOUSEBUTTONDOWN 
import time
from board import * 

pygame.init()
pygame.display.init()
 
def insertDisc(x):
    global turn
    for y in range(1, 7):
        if Board.holes[-y][x] == 0:
            turn += 1
            if turn % 2 == 0:
                Board.holes[-y][x] = 1
                break
            else:
                Board.holes[-y][x] = 2
                break

DISPLAY = (700, 600)
WHITE = (255, 255, 255)
holeColour = (18, 18, 20)
BLOO = (45, 93, 215)
RED = (215, 38, 61)
YELLOW = (214, 187, 31)
hlColour = (124, 45,  215)
gridColour = (50, 50, 255)
title = pygame.display.set_caption("Connect four")
window = pygame.display.set_mode(DISPLAY)
Board = board(window)
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",50)
turn = 1

run = True

while run:
    pygame.time.Clock().tick(100)
    window.fill(BLOO)
    posx = pygame.mouse.get_pos()[0] // 100
    posy = pygame.mouse.get_pos()[1] // 100
    Board.Highlight(hlColour, posx)
    Board.DrawGrid(gridColour)
    Board.DrawCircles(holeColour, RED, YELLOW)
    Board.CheckWin(window, font, DISPLAY)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            xPos = pygame.mouse.get_pos()[0] // 100
            insertDisc(xPos)

        if event.type == pygame.QUIT:
            run = False
        
        if Board.win == True:
            time.sleep(7.5)
            run = False
        
    
        
