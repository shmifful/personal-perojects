##started: 17/11/2020
##finished:

import pygame
import random

###OBJECTS
class Hover:
    def __init__(self, win):
        self.win = win
        self.clicked = None
        self.tap = [None, None]
        
    def click(self, event, font, pos):
        if event.type == pygame.MOUSEBUTTONDOWN: #checks if left mouse button has been pressed
            pass

class Numbers:
    def __init__(self):
        pass
    
        
###FUNCTIONS
def grid(win, colour): #for every 50 lines on the window, a line is been drawn
    x = 1
    y = 1
    for i in range(0,500,50):
        #draws bolder lines to seperate boxes
        if i % 150 == 0:
            width = 5
        else:
            width = 1
        pygame.draw.line(win, (colour), (x*i, y), (x*i, 450), width)#draws horizontal lines
        pygame.draw.line(win, (colour), (x, y*i), (450, y*i), width)#draws vertical lines
    
def highlight(POS): #gets the position of the mouse and highlights the squares
    X = POS[0]//50
    Y = POS[1]//50
    pygame.draw.rect(win, (255, 228, 127), (X*50, Y*50, 50, 50))

def sudoku(board, win):
    for i in range(0, 9):
        for j in range(0, 9):
            text = font.render(str(board[i][j]), True, (0,0,0))
            textRect = text.get_rect()
            textRect.center = (i*50+25, j*50+27)
            win.blit(text, textRect)

##sudoku logic#######################################################################################################################
base  = 3
side  = base*base

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
from random import sample
def shuffle(s): return sample(s,len(s)) 
rBase = range(base) 
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

# produce board using randomized baseline pattern
board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
newBoard = [[],[],[],[],[],[],[],[],[]]
##sudoku logic#######################################################################################################################

for i in range(0,9):
    for j in range(0, 9):
        ran = random.randint(1,9)
        if ran%2 == 0: ###there is one in 4 chances that a square will be empty
            newBoard[i].append("")
        else:
            newBoard[i].append(board[i][j])

###CONSTANTS & VARIABLES
SCREENSIZE = (450,450)
WHITE = (255,255,255)
BLACK = (0,0,0)
clock = pygame.time.Clock()


###GAME
pygame.init() 
pygame.font.init()
win = pygame.display.set_mode(SCREENSIZE)
title = pygame.display.set_caption("SUDOKU")
update = pygame.display.update()
running = True
font = pygame.font.SysFont("Calibri", 45)
mouse = Hover(win)
clicked = [None, None]


while running:
    POS = pygame.mouse.get_pos() #getting the position of the mouse
    win.fill(WHITE)
     
    clock.tick(60)
    pygame.display
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: #checks if left mouse button has been pressed
            clicked = POS #checking if mouse has been clicked
            
        if event.type == pygame.KEYDOWN:
            if event.unicode != "0":
                t = event.unicode

        if event.type == pygame.QUIT:
            running = False

    if pygame.key.get_pressed()[pygame.K_SPACE]:

        for i in range(0,9):
            for j in range(0,9):
                while str(newBoard[j][i]) != str(board[j][i]):
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
        
                    win.fill(WHITE)
                    clock.tick(20)
                    t = random.randint(1,9)
                    pygame.draw.rect(win, (255, 0, 0), (j*50, i*50, 50, 50))
                    newBoard[j][i] = t
                    sudoku(newBoard, win)
                    grid(win, BLACK)
                    pygame.display.update()

    highlight(POS) #highlights the square the mouse is hovering over
    if clicked[0] != None and clicked[1] != None:
        pygame.draw.rect(win, (255, 200, 100), (clicked[0]//50*50, clicked[1]//50*50, 50, 50))

        

    try:
        trial = int(t)

        if str(newBoard[clicked[0]//50][clicked[1]//50]) != str(board[clicked[0]//50][clicked[1]//50]):
            pygame.draw.rect(win, (255, 0, 0), (clicked[0]//50*50, clicked[1]//50*50, 50, 50))
            newBoard[clicked[0]//50][clicked[1]//50] = t

        if str(newBoard[clicked[0]//50][clicked[1]//50]) == str(board[clicked[0]//50][clicked[1]//50]):
           pygame.draw.rect(win, (0, 255, 0), (clicked[0]//50*50, clicked[1]//50*50, 50, 50)) 
           
        
   
    except TypeError:
        pass
    except  NameError:
        pass
    except ValueError:
        pass
    sudoku(newBoard, win)

    grid(win, BLACK) #creates grid

    pygame.display.update()

pygame.quit()

