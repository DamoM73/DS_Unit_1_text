from tkinter import *
import time
import random

WIDTH = 800
HEIGHT = 500
SIZE = 20

def lmc(event):
    Ball(event.x, event.y)

class Ball:
    def __init__(self, x, y):
        self.shape = canvas.create_oval(x, y, x+SIZE, y+SIZE, fill=color)
        self.speedx = random.randrange(-10,10)
        self.speedy = random.randrange(-10,10)
        self.active = True
        self.move_active()

    def ball_update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

    def move_active(self):
        if self.active:
            self.ball_update()
            root.after(40, self.move_active) 

root = Tk()
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="grey")
canvas.pack()
canvas.bind("<Button-1>",lmc)
color = 'red'

root.mainloop()