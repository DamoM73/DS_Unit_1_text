from tkinter import *

# CONSTANTS
WIDTH = 1000
HEIGHT = 600

# CLASSES

# FUNCTIONS

# GLOBAL VARIABLES
diameter = 0
total = 0
f1 = 0
f2 = 1
numberOfBubbles = 0
x1 = 0                                                      # the left most x value of the circle
y1 = HEIGHT                                                 # the left most y value of the circle

# INITIALISE TKINTER
tk = Tk()                                                   # create a tk object
canvas = Canvas(tk, width = WIDTH, height = HEIGHT)         # create a canvas on the object
tk.title("Fibonacci Bubbles")                               # change the window title
canvas.pack()                                               # display the canvas

while True:
    total = f1 + f2
    diameter = total
    f2 = f1
    f1 = total
    
    if numberOfBubbles < 14:
        x2 = x1 + diameter
        y2 = y1 - diameter
        canvas.create_oval(x1,y1,x2,y2, fill="blue")
        x1 = x2
        numberOfBubbles += 1
    tk.update()    


tk.mainloop()                                               #continue to display the canvas