from tkinter import *

class Bubble():
    def __init__(self,x,y):
        self.x1 = x-10
        self.y1 = y-10
        self.x2 = x+10
        self.y2 = y+10

def left_mouse_click(event):
    new_bubble = Bubble(event.x, event.y)
    main_canvas.create_oval(new_bubble.x1,new_bubble.y1,new_bubble.x2,new_bubble.y2,fill="red")
    main_canvas.update()
    bubbles.append(new_bubble)
    
def bubble_update():
    index = 0
    while index < len(bubbles):
        main_canvas.move(bubbles[index],10,0)
        if bubbles[index].y1 > HEIGHT:
            bubbles.pop(index)
    main_canvas.update()
    root.after(100, bubble_update)
            

WIDTH = 600
HEIGHT = 400

bubbles = []

# **** Create window ****
root = Tk()
root.title("bouncing Bubbles")

# **** Add content to window ****
main_canvas = Canvas(root, width=WIDTH, height = HEIGHT, bg="white")
main_canvas.pack(fill=BOTH, expand=YES)
main_canvas.bind("<Button-1>",lmc)


# **** Run window loop ****
root.after(100, bubble_update)
root.mainloop()