from tkinter import *

# CONSTANTS
WIDTH = 1000
HEIGHT = 600

# GLOBAL VARIABLES
total = 0
f1 = 0
f2 = 1
numberOfBubbles = 0
x1 = 0                                                  # the left most x value of the circle
y1 = HEIGHT                                             # the bottom most y value

# INITIALISE TKINTER
window = Tk()                                           # creates a window
canvas = Canvas(window, width=WIDTH, height=HEIGHT)     # create a canvas to draw on
window.title("Fibonacci Bubble")                        # change the window title
canvas.pack()                                           # put the canvas in the window

while numberOfBubbles < 14:
    total = f1 + f2
    f2 = f1

    f1 = total
    diameter = total

    numberOfBubbles += 1

    x2 = x1 + diameter
    y2 = y1 - diameter
    canvas.create_oval(x1,y1,x2,y2, fill="blue")
    x1 = x2
    window.update()

window.mainloop()