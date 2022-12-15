import pygame as pg
import numpy as np
from math import factorial, isclose


def clear_and_redraw():
    screen.fill((255, 255, 255))
    for i in range(count - 1):
        pg.draw.line(screen, (0, 255, 0), points[i], points[i+1], 3)
    for i in range(count):
        pg.draw.rect(screen, (0, 0, 255), (points[i][0] - margin, points[i][1] - margin, 2 * margin, 2 * margin), 5)


def bezier():
    clear_and_redraw()
    length = len(points)
    n = length - 1
    for t in np.arange(0, 1, 0.01):
        z = np.zeros(2)
        for i in range(length):
            z += np.dot((factorial(n)/(factorial(i)*factorial(n-i)))
                        *((1-t)**(n-i))*(t**i),points[i])

        pg.draw.circle(screen, (255, 0, 0), z.astype(int), 2)
    

def draw_polylines(color='GREEN', thick=3):
    if (count < 2): return
    for i in range(count - 1):
        pg.draw.line(screen, color, points[i], points[i+1], thick)
    for i in range(count):
        pg.draw.rect(screen, (0, 0, 255), (points[i][0] - margin, points[i][1] - margin, 2 * margin, 2 * margin), 5)
        bezier()


size = [800, 800]
pg.init()
screen = pg.display.set_mode(size, 0, 32)
pg.display.set_caption("9371_Egorov_Lab2")
screen.fill((255, 255, 255))

points = []
count = 0

done = False
pressed = 0
margin = 5
old_pressed = 0
old_button1 = 0
old_button3 = 0
selected_point = -1

while not done:
    for event in pg.event.get():
        pos = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            pressed = -1
            if count > 2:
                bezier()
        elif event.type == pg.MOUSEBUTTONUP:
            pressed = 1
        elif event.type == pg.QUIT:
            done = True
        else:
            pressed = 0
        
    button1, button2, button3 = pg.mouse.get_pressed()
    x, y = pg.mouse.get_pos()
    point = [x, y]

    if old_pressed == -1 and pressed == 1 and old_button1 == 1 and button1 == 0:
        points.append(point)
        count += 1
        pg.draw.rect(screen, (0, 0, 255), (point[0] - margin, point[1] - margin, 2 * margin, 2 * margin), 5)
    elif old_pressed == -1 and pressed == -1 and old_button1 == 1 and button1 == 1:
        for i in range(len(points)):
            if((isclose(x, points[i][0], rel_tol=0.05)) and (isclose(y, points[i][1], rel_tol=0.05))):
                selected_point = i
    elif old_pressed == 0 and pressed == 0 and old_button1 == 1 and button1 == 1:
        if selected_point != -1:
            screen.fill((255, 255, 255))
            points[selected_point][0] = x
            points[selected_point][1] = y
    elif old_pressed == 1 and pressed == 1 and old_button1 == 0 and button1 == 0:
        selected_point = -1
    elif old_pressed == -1 and pressed == 1 and old_button3 == 1 and button3 == 0:
        for i in range(len(points)):
            if((isclose(x, points[i][0], rel_tol=0.05)) and (isclose(y, points[i][1], rel_tol=0.05))):
                del points[i]
                count -= 1
                screen.fill((255, 255, 255))
                break
    if len(points) > 1:
        draw_polylines((0, 255, 0), 3)
    
    pg.display.update()
    old_button1 = button1
    old_pressed = pressed
    old_button3 = button3

pg.quit()
