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
bubbleX = 0
bubbleY = HEIGHT
x1 = bubbleX
y1 = bubbleY

# INITIALISE TKINTER
tk = Tk()                                                  # create a tk object
canvas = Canvas(tk, width = WIDTH, height = HEIGHT)        # create a canvas on the object
tk.title("Name")                                            # change the window title
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


tk.mainloop()                                           #continue to display the canvas