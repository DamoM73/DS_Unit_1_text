from tkinter import *

# CONSTANTS
WIDTH = 800
HEIGHT = 600

# GLOBAL VARIABLES
floor = [150,345]

# CLASSES

# FUNCTIONS

# Uses Euclid's algortihm to fiund the perfect size sqare tile for given room
def calculateTileSize(floor):
    tileWidth = floor[0]
    tileLength = floor[1]
    while True:
        remainder = tileLength % tileWidth
        if remainder == 0:
            return tileWidth
        else:
            tileLength = tileWidth
            tileWidth = remainder
   

# Displays tiles for a given room size
def displayFloor(floor, tile):
    # initialise variables
    floorWidth = floor[0]
    floorLength = floor[1]
    countTilesX = 0
    countTilesY = 0
    numberOfTilesX = floorLength / tile
    numberOfTitesY = floorWidth / tile
    x1 = 0
    y1 = 0

    # generate tiles
    while (countTilesY < numberOfTitesY): 
        if countTilesX < numberOfTilesX:
            x1 = countTilesX * tile
            y1 = countTilesY * tile
            x2 = x1 + tile
            y2 = y1 + tile
            canvas.create_rectangle(x1, y1, x2, y2)
            countTilesX += 1
        else:
            countTilesY += 1
            countTilesX = 0

# Display details of the tile
def displayTileSize(floor, tile):
    floorWidth = floor[0]
    floorLength = floor[1]
    numberOfTilesX = floorLength / tile
    numberOfTitesY = floorWidth / tile
    canvas.create_text(WIDTH/2, HEIGHT - 40, text="Your perfect square tile has the dimension of " + str(tile) + " cm sqaure")
    canvas.create_text(WIDTH/2, HEIGHT - 20, text="You need " + str(int(numberOfTilesX * numberOfTitesY)) + " tiles")


# INITIALISE TKINTER
window = Tk()                                               # create a tk object
canvas = Canvas(window, width = WIDTH, height = HEIGHT)         # create a canvas on the object
window.title("Euclid's Tiles")                              # change the window title
canvas.pack()                                               # display the canvas

tileSize = calculateTileSize(floor)
displayFloor(floor, tileSize)
displayTileSize(floor, tileSize)


window.mainloop()                                               #continue to display the canvas