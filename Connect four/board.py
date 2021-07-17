import pygame
import time

class board:
    def __init__(self, surface):
        #if self.hole[y][x] = 0 then hole = black, if self.hole[y][x] = 1 then hole = coloured
        self.holes = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]]
        self.surface = surface
        self.winner = ""
        self.win = False

    def Highlight(self, colour, x):
        pygame.draw.line(self.surface, colour, ((x*100)+50, 0), ((x*100)+50, 600), 100)

    def DrawGrid(self, colour):
        for i in range(1, 7):
            pygame.draw.line(self.surface, colour, (0, i*100), (700, i*100))
            pygame.draw.line(self.surface, colour, (i*100, 0), (i*100, 700))

    def DrawCircles(self, hollowColour, red, yellow):
        for x in range(0, 7):
            for y in range(0, 6):
                if self.holes[y][x] == 0:
                    pygame.draw.circle(self.surface, hollowColour, ((x*100)+50, (y*100)+50), 35)

                if self.holes[y][x] == 1:
                    pygame.draw.circle(self.surface, red, ((x*100)+50, (y*100)+50), 35)

                if self.holes[y][x] == 2:
                    pygame.draw.circle(self.surface, yellow, ((x*100)+50, (y*100)+50), 35)

    def CheckWin(self, win, font, size):
        for x in range(0, 7):
            for y in range(0, 6):
                try:
                    if self.holes[y][x] != 0:
                        if self.holes[y][x] == 1 and self.holes[y][x+1] == 1 and self.holes[y][x+2] == 1 and self.holes[y][x+3] == 1:
                            self.winner = "Red"
                        if self.holes[y][x] == 2 and self.holes[y][x+1] == 2 and self.holes[y][x+2] == 2 and self.holes[y][x+3] == 2:
                            self.winner = "Yellow"

                        if self.holes[y][x] == 1 and self.holes[y+1][x] == 1 and self.holes[y+2][x] == 1 and self.holes[y+3][x] == 1:
                            self.winner = "Red"
                        if self.holes[y][x] == 2 and self.holes[y+1][x] == 2 and self.holes[y+2][x] == 2 and self.holes[y+3][x] == 2:
                            self.winner = "Yellow"

                        if self.holes[y][x] == 1 and self.holes[y+1][x+1] == 1 and self.holes[y+2][x+2] == 1 and self.holes[y+3][x+3] == 1:
                            self.winner = "Red"
                        if self.holes[y][x] == 2 and self.holes[y+1][x+1] == 2 and self.holes[y+2][x+2] == 2 and self.holes[y+3][x+3] == 2:
                            self.winner = "Yellow"
                        
                        if self.holes[y][x] == 1 and self.holes[y+1][x-1] == 1 and self.holes[y+2][x-2] == 1 and self.holes[y+3][x-3] == 1:
                            self.winner = "Red"
                        if self.holes[y][x] == 2 and self.holes[y+1][x-1] == 2 and self.holes[y+2][x-2] == 2 and self.holes[y+3][x-3] == 2:
                            self.winner = "Yellow"
                        
                        if self.holes[5][3] == 1 and self.holes[4][4] == 1 and self.holes[3][5] == 1 and self.holes[2][6] == 1:
                            self.winner = "Red"
                        if self.holes[5][3] == 2 and self.holes[4][4] == 2 and self.holes[3][5] == 2 and self.holes[2][6] == 2:
                            self.winner = "Yellow"

                    if self.winner != "":
                        textWinner = f"{self.winner} is the winner!"
                        renderText = font.render(textWinner, True, (50,205,50), None)
                        textRect = renderText.get_rect()
                        textRect.center = (size[0]/2, size[1]/2)
                        win.blit(renderText, textRect)
                        self.win = True
                        
                except IndexError:
                    pass
            

 

