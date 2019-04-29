''' Example of how to animate in tkinter '''
from tkinter import *
from random import *

WIDTH = 600
HEIGHT = 400
SIZE = 10

speedx= randrange(-10,10)
speedy= randrange(-10,10)

# **** Functions ****
def move_ball():
    global speedx, speedy
    main_canvas.move(ball, speedx, speedy)
    pos = main_canvas.coords(ball)
    if pos[2] >= WIDTH or pos[0] <= 0:
        speedx *= -1
    if pos[3] >= HEIGHT or pos[1] <= 0:
        speedy *= -1
    root.after(40,move_ball)


# **** Create Window ****
root = Tk()
root.title("Animation Example")

# **** Add content to window ****
main_canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
main_canvas.pack()
ball = main_canvas.create_oval(WIDTH/2-SIZE, HEIGHT/2-SIZE, WIDTH/2+SIZE, HEIGHT/2+SIZE, fill="orange")

# **** Run window loop ****
root.after(40,move_ball)
root.mainloop()