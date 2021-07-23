import pygame
import random
import time

def create_rectangle_heights(x, max_height):
    height_list = [] 
    for i in range(0, x):
        height = random.randint(0, max_height)
        height_list.append(height)
    
    return height_list

def sort(surface, colour, list, width, y):
    for i in range(1, len(list)):
        surface.fill((0, 0, 0))
        for n in range(len(list)):
            pygame.draw.line(surface, (75, 100, 255), ((n*10)+5, y - list[n]), ((n*10)+5, y), width)

        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            pygame.draw.line(surface, (75, 255, 100), ((j*10)+5, y - list[j]), ((j*10)+5, y), width)
            pygame.draw.line(surface, colour, (((j+1)*10)+5, y - list[j+1]), (((j+1)*10)+5, y), width)
            pygame.display.update()
            list[j+1] = list[j]
            j -= 1
            time.sleep(0.05)
        list[j+1] = key

screensize = (500, 250)
running = True
rectangle_width = 9
BLUE = (75, 125, 255)
RED = (255, 45, 50)
x = int(screensize[0]/10)
y = int(screensize[1])
height_list = create_rectangle_heights(x, y)

pygame.init()
window = pygame.display.set_mode(screensize)
title = pygame.display.set_caption("Bubble sort")

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        sort(window, RED, height_list, rectangle_width, y)
        window.fill((0, 0, 0))
        for j in range(len(height_list)):
            pygame.draw.line(window, (75, 100, 255), ((j*10)+5, y - height_list[j]), ((j*10)+5, y), rectangle_width)
        pygame.display.update()
        time.sleep(2.5)
        running = False