import pgzero
import sys
import pygame
HEIGHT=500
WIDTH=500
x_axis=150
y_axis=150
radius=50
reverse=False
def draw():
    screen.fill('black')
    screen.draw.circle((x_axis,y_axis),radius,'green')
def update():
    global y_axis,x_axis,reverse
    if y_axis==450:
        reverse=True
    elif y_axis==50:
        reverse=False
    elif y_axis<450 and reverse==False:
        y_axis+=1
    elif y_axis>50 and reverse==True:
        y_axis-=1

