from tkinter import *

# CONSTANTS
WIDTH = 800
HEIGHT = 600

# CLASSES

# FUNCTIONS

# GLOBAL VARIABLES

# INITIALISE TKINTER
tk = Tk()                                                   # create a tk object
canvas = Canvas(tk, width = WIDTH, height = HEIGHT)         # create a canvas on the object
tk.title("Name")                                            # change the window title
canvas.pack()                                               # display the canvas

tk.mainloop()                                               #continue to display the canvas