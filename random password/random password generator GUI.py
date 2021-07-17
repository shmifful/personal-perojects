import random
from tkinter import *


def generate():
    password = ""
    p = []
    for i in range(127):
        p.append(chr(i))
            
    for i in range(8):
        r = random.randint(33, 126)
        password += str(p[r])
            
    Label(win, text = password).grid(row = 0, column = 0, padx = 70)
        
win = Tk()

win.geometry("200x100")
win.title("RPG")
Button(win, text = "Generate", command = generate).grid(row = 2, column = 0, padx = 70, pady = 20)

win.mainloop()
    
