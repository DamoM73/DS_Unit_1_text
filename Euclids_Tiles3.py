from tkinter import *

# CONSTANTS
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

# GLOBAL VARIABLES
room_long = 345
room_short = 150

# FUNCTIONS
# calculate tile size
def calculate_tile_size(tile_long, tile_short):
    while True:
        remainder = tile_long % tile_short
        if remainder == 0:
            return tile_short
        else:
            tile_long = tile_short
            tile_short = remainder
    
# calculate number of tiles X and Y
def calculate_num_of_tiles(room_width, room_height, tile):
    number_of_tiles_X = room_width // tile
    number_of_tiles_Y = room_height // tile
    return [number_of_tiles_X,number_of_tiles_Y]


# display the floor
def display_floor(num_of_tiles, tile, canvas):
    # initialise variables
    x1 = 0
    y1 = 0

    # generate tiles on canvas
    for count_y_tiles in range(0,num_of_tiles[1]):
        for count_x_tiles in range(0,num_of_tiles[0]):
            x1 = count_x_tiles * tile
            y1 = count_y_tiles * tile
            x2 = x1 + tile
            y2 = y1 + tile
            canvas.create_rectangle(x1,y1,x2,y2, fill="light blue")

# display tile size
def display_tile_size(num_of_tiles, tile, canvas):
    # initalise vaiables
    canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT - 40, text="Yoour perfect square tile has a side of " + str(tile) + " cm.")
    canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT -20, text="You will need " + str(num_of_tiles[0] * num_of_tiles[1]) + " tiles.")


# ---- MAIN PROGRAM ----

# INITIALISE TKINTER
window = Tk()
window.title("Euclid's Tiles")
canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

tile_size = calculate_tile_size(room_long, room_short)
num_of_tiles = calculate_num_of_tiles(room_long, room_short, tile_size)
display_floor(num_of_tiles, tile_size, canvas)
display_tile_size(num_of_tiles, tile_size, canvas)

window.mainloop()