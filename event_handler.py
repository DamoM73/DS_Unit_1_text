from tkinter import *

# CONSTANTS
WIDTH = 800
HEIGHT = 600
COLOURS = ["red", "yellow", "pink", "green", "blue"]

# GLOBAL VARIABLES
index = 0
# CLASSES

# FUNCTIONS
def callback(event):
    global index
    index += 1
    if index > len(COLOURS) -1:
        index = 0
    draw()

def draw():
    canvas.delete("all")
    canvas.create_text(WIDTH/2, HEIGHT/2, text=COLOURS[index], fill=COLOURS[index])
    


# INITIALISE TKINTER
tk = Tk()                                                   # create a tk object
canvas = Canvas(tk, width = WIDTH, height = HEIGHT)         # create a canvas on the object
tk.title("Event Handler")                                   # change the window title
canvas.bind("<Button-1>", callback)
canvas.pack()                                               # display the canvas

draw()

tk.update
tk.mainloop()                                               #continue to display the canvas