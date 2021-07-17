#####TIC TAC TOE~~~~~
###date started: 14.08.2020
###date finished:

import pygame
from pygame import *
from tkinter import *
import time
import random
import sqlite3

#functions
def main():
    def PVP_and_destroy():
        display.destroy()
        PVP()

    def AI_and_destroy():
        display.destroy()
        AI()

    def multiplayer_and_destroy():
        display.destroy()
        multiplayer()
        
    display = Tk()
    
    display.title("MENU")
    display.geometry("300x300")
    display.config(bg="black")

    Label(display, text = "Welcome to TIC TAC TOE", fg = "white", bg = "blue", font = (15)).pack()
    Button(display, text = "PvP", width = 15, command = PVP_and_destroy).pack(pady = 35)
    Button(display, text = "A.I.", width = 15, command = AI_and_destroy).pack()
    Button(display, text = "Multiplayer", width = 15, command = multiplayer_and_destroy).pack(pady = 35)
    Button(display, text = "EXIT", width = 15, command = exit).pack()
    
    display.mainloop()

def grid(win):
    x = 0
    y = 0
    for i in range(2):
        x += 150
        y += 150
        pygame.draw.line(win, (255,255,255), (x,0), (x,450))#draws vertical lines
        pygame.draw.line(win, (255,255,255), (0,y), (450,y))#draws horizontal lines

def playerTurn(posX, posY, turn, square, win, font, game):
    #looking at the first square
    if posX == 0 and posY == 0 and square[0] == 1:
        if turn%2 == 0:
            text = font.render("X", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (75,75)
            win.blit(text, textRect)
            square[0] = "X"
        else:
            text = font.render("O", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (75,75)
            win.blit(text, textRect)
            square[0] = "O"
    #looking at the second square
    if posX == 1 and posY == 0 and square[1] == 2:
        if turn%2 == 0:
            text = font.render("X", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (225,75)
            win.blit(text, textRect)
            square[1] = "X"
        else:
            text = font.render("O", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (225,75)
            win.blit(text, textRect)
            square[1] = "O"
    #looking at the third square
    if posX == 2 and posY == 0 and square[2] == 3:
        if turn%2 == 0:
            text = font.render("X", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (375,75)
            win.blit(text, textRect)
            square[2] = "X"
        else:
            text = font.render("O", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (375,75)
            win.blit(text, textRect)
            square[2] = "O"

    #looking at the fourth square
    if posX == 0 and posY == 1 and square[3] == 4:
        if turn%2 == 0:
            text = font.render("X", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (75,225)
            win.blit(text, textRect)
            square[3] = "X"
        else:
            text = font.render("O", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (75,225)
            win.blit(text, textRect)
            square[3] = "O"
    #looking at the fifth square
    if posX == 1 and posY == 1 and square[4] == 5:
        if turn%2 == 0:
            text = font.render("X", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (225,225)
            win.blit(text, textRect)
            square[4] = "X"
        else:
            text = font.render("O", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (225,225)
            win.blit(text, textRect)
            square[4] = "O"
    #looking at the sixth square
    if posX == 2 and posY == 1 and square[5] == 6:
        if turn%2 == 0:
            text = font.render("X", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (375,225)
            win.blit(text, textRect)
            square[5] = "X"
        else:
            text = font.render("O", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (375,225)
            win.blit(text, textRect)
            square[5] = "O"

    #looking at the seventh square
    if posX == 0 and posY == 2 and square[6] == 7:
        if turn%2 == 0:
            text = font.render("X", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (75,375)
            win.blit(text, textRect)
            square[6] = "X"
        else:
            text = font.render("O", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (75,375)
            win.blit(text, textRect)
            square[6] = "O"
    #looking at the eigth square
    if posX == 1 and posY == 2 and square[7] == 8:
        if turn%2 == 0:
            text = font.render("X", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (225,375)
            win.blit(text, textRect)
            square[7] = "X"
        else:
            text = font.render("O", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (225,375)
            win.blit(text, textRect)
            square[7] = "O"
    #looking at the last square
    if posX == 2 and posY == 2 and square[8] == 9:
        if turn%2 == 0:
            text = font.render("X", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (375,375)
            win.blit(text, textRect)
            square[8] = "X"
        else:
            text = font.render("O", True, (255,0,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (375,375)
            win.blit(text, textRect)
            square[8] = "O"
    pygame.display.update()

        ###win screen##############
    def yes():
        if game == 1:
            pygame.quit()
            winScreen.destroy()
            PVP()
        if game == 2:
            pygame.quit()
            winScreen.destroy()
            AI()

    def no():
        pygame.quit()
        winScreen.destroy()
        main()
            
    if square[0] == square[1] and square[1] == square[2] or square[3] == square[4] and square[4] == square[5] or square[6]== square[7] and square[7] == square[8] or square[0] == square[3] and square[3] == square[6] or square[1] == square[4] and square[4] == square[7] or square[2] == square[5] and square[5] == square[8] or square[0] == square[4] and square[4] == square[8] or square[2] == square[4] and square[4] == square[6]:
        winScreen = Tk()
        winScreen.geometry("350x100")
        winScreen.title("Winner!")
        running = False
            
        winner = ""
        if turn%2 == 0:
            winner = "X"
        else:
            winner = "O"
        Label(winScreen, text = winner + "'s the WINNER!\nDo you want to play again?", font=(5)).grid(row = 0, column = 1)
        Button(winScreen, text = "Yes", width = 10, command = yes).grid(row = 1, column = 0)
        Button(winScreen, text = "No", width = 10, command = no).grid(row = 1, column = 1)
        Button(winScreen, text = "EXIT", width = 10, command = exit).grid(row = 1, column = 2)
                    
        winScreen.mainloop()

def PVP():
    game = 1## specifying which mode the player is playing in
    screen = (450,450)
    pygame.init()
    font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",150)
    clock = pygame.time.Clock()
    win = pygame.display.set_mode(screen)#creates display
    title = pygame.display.set_caption("GAME")
    update = pygame.display.update()
    running = True
    square = [1,2,3,4,5,6,7,8,9]
    turn = 1
    
    while running:
        clock.tick(10)
        grid(win)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:#checks if the cross is being clicked
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:#sees if any button from the mouse is pressed
                    pos = pygame.mouse.get_pos()
                    #simplifying which box the mouse clicks
                    posX = pos[0]//150
                    posY = pos[1]//150
                    playerTurn(posX, posY, turn, square, win, font, game)
                    turn += 1
                    
                    
        pygame.display.update()#updates the display
    pygame.quit()#closes the window
    main()
    
def AI():
    ###normal mode does not have much coding, but it plays randomly
    def normal():
        optionWin.destroy()
        def first():
            choiceWin.destroy()
            screen = (450, 450)
            pygame.init()
            font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",150)
            clock = pygame.time.Clock()
            win = pygame.display.set_mode(screen)#creates display
            title = pygame.display.set_caption("GAME")
            update = pygame.display.update()
            running = True
            square = [1,2,3,4,5,6,7,8,9]
            posX = None
            posY = None
            botPos = []
            turn = 1
    
            while running:
                clock.tick(10)
                grid(win)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:#checks if the cross is being clicked
                                running = False
                        if turn%2 == 0:
                                posX = random.randint(0,2)
                                posY = random.randint(0,2)
                                while [posX,posY] in botPos:
                                    posX = random.randint(0,2)
                                    posY = random.randint(0,2)

                                botPos.append([posX,posY])
                                playerTurn(posX, posY, turn, square, win, font, game)
                                turn += 1
                                
                        if turn%2 !=0:
                            if event.type == pygame.MOUSEBUTTONDOWN:#sees if any button from the mouse is pressed
                                pos = pygame.mouse.get_pos()
                                #simplifying which box the mouse clicks
                                posX = pos[0]//150
                                posY = pos[1]//150
                                botPos.append([posX,posY])
                                playerTurn(posX, posY, turn, square, win, font, game)
                                turn += 1
        
                        pygame.display.update()
        def second():
            choiceWin.destroy()
            screen = (450, 450)
            pygame.init()
            font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",150)
            clock = pygame.time.Clock()
            win = pygame.display.set_mode(screen)#creates display
            title = pygame.display.set_caption("GAME")
            update = pygame.display.update()
            running = True
            square = [1,2,3,4,5,6,7,8,9]
            posX = None
            posY = None
            botPos = []
            turn = 1
    
            while running:
                clock.tick(10)
                grid(win)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:#checks if the cross is being clicked
                                running = False
                        if turn%2 != 0:
                                posX = random.randint(0,2)
                                posY = random.randint(0,2)
                                while [posX,posY] in botPos:
                                    posX = random.randint(0,2)
                                    posY = random.randint(0,2)

                                botPos.append([posX,posY])
                                playerTurn(posX, posY, turn, square, win, font, game)
                                turn += 1
                                
                        if turn%2 ==0:
                            if event.type == pygame.MOUSEBUTTONDOWN:#sees if any button from the mouse is pressed
                                pos = pygame.mouse.get_pos()
                                #simplifying which box the mouse clicks
                                posX = pos[0]//150
                                posY = pos[1]//150
                                botPos.append([posX,posY])
                                playerTurn(posX, posY, turn, square, win, font, game)
                                turn += 1
        
                        pygame.display.update()
            
        choiceWin = Tk()

        choiceWin.geometry("250x105")
        choiceWin.title("Choice")

        Label(choiceWin, text = "As what player do you\nwant to start as?").pack()
        Button(choiceWin, text = "First (O)", width = 15, command = first).pack(pady = 5)
        Button(choiceWin, text = "Second (X)", width = 15, command = second).pack()
        
        choiceWin.mainloop()

    def hard():
        optionWin.destroy()

        def first():
            pass

        def second():
            pass

        def main_and_destroy():
            choiceWin.destroy()
            main()

        ####the block of code below has been copied and pasted because i could not put it in a function
        choiceWin = Tk()

        choiceWin.geometry("250x105")
        choiceWin.title("Choice")

        Label(choiceWin, text = "Sorry...\nThis game mode is yet not available.").pack()
        Button(choiceWin, text = "Return to Menu", width = 15, command = main_and_destroy).pack(pady = 15)
        
        choiceWin.mainloop()

    ##~MAIN PROGRAM~##
    ###on this window, the player chooses which mode they want to play in
    game = 2###to specify what mode the player is playing
    optionWin = Tk()

    optionWin.geometry("175x105")
    optionWin.title("Option")

    Button(optionWin, text = "Normal", command = normal, width = 15).pack(pady = 15)
    Button(optionWin, text = "Hard", command = hard, width = 15).pack()

    optionWin.mainloop()

def multiplayer():
    def login():
        mulWin.destroy()
        pass

    def register():
        ##initialising sqlite
        con = sqlite3.connect("userData.db")
        c = con.cursor()
        def submit():
            #creating tables in the database
            def createTable():
                c.execute("CREATE TABLE IF NOT EXISTS userInfo(username TEXT PRIMARY KEY, password TEXT)")

            def dataRead():
                username = user.get()
                password = pword.get()

                c.execute('SELECT username FROM userInfo WHERE username = ?', (username,))
                data = c.fetchone()
                if data:
                    Label(regWin, text = "Sorry, username already in use...\nTry another one.", fg = "red").pack()
                    print(data)
                else:
                    dataEntry(username, password)
                #except TypeError:
                    #dataEntry(username, password)
                    
            def dataEntry(username, password):
                c.execute("INSERT INTO userInfo(username, password) VALUES (?, ?)", (username, password))
                con.commit()
                
            createTable()
            dataRead()
        
        mulWin.destroy()
        regWin = Tk()

        regWin.geometry("250x200")
        regWin.title("Register")

        Label(regWin, text = "Register", font = (20)).pack(pady = 5)
        Label(regWin, text = "Username:").pack()
        user = Entry(regWin, width = 30)
        user.pack(pady = 3)
        Label(regWin, text = "Password:"). pack(pady = 3)
        pword = Entry(regWin, width = 30, show = "*")
        pword.pack()
        Button(regWin, text = "SUBMIT", command = submit).pack(pady = 8)

        regWin.mainloop()
    
    mulWin = Tk()

    mulWin.geometry("250x150")
    mulWin.title("User option")
    #giving the user a choice to log in or register
    Label(mulWin, text = "Hello user!").pack(pady = 5)
    Button(mulWin, text = "Log in", width = 10, command = login).pack(pady = 10)
    Button(mulWin, text = "Register", width = 10, command = register).pack()
    Button(mulWin, text = "Exit", width = 10, command = exit).pack(pady = 10)

    mulWin.mainloop()

#main program
# 1 = PVP
# 2 = AI
game = None
main()
