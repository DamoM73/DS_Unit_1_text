from tkinter import *

WIDTH = 600
HEIGHT = 400
SIZE = 10

class bubble():

    def __init__(self,event):
        self.x1 = event.x-SIZE
        self.y1 = event.y-SIZE
        self.x2 = event.x+SIZE
        self.y2 = event.y+SIZE
        self.shape = main_canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")
        self.speedy = 0
        self.move_bubble()

    def bubble_update(self):
        main_canvas.move(self.shape, 0, self.speedy)
        pos = main_canvas.coords(self.shape)
        
        if pos[3] >= HEIGHT and self.speedy > 1:        
            self.speedy = round((self.speedy - 1) * -1,1)
        elif pos[3] >= HEIGHT and self.speedy <= 1:
            self.speedy = 0
        else:
            self.speedy += .1
    
    def move_bubble(self):
        self.bubble_update()
        root.after(20, self.move_bubble)


def lmc_task(event):
    bubble(event)


# **** Create window ****
root = Tk()
root.title("Bouncing Bubbles")

# **** Add content to the window ****
main_canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
main_canvas.pack()
main_canvas.bind("<Button-1>", lmc_task)


# **** Run window loop ****
root.mainloop()