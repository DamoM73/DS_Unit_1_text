# Pygame template - skeleton for a new pygame project
# --- IMPORT LIBARIES
import pygame
import random

# --- DECLARE CONSTANTS
# screen constants
WIDTH = 640                                             # Screen width
HEIGHT = 480                                            # Screen Height
FPS = 30                                                # Frames per second

# basic colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# --- DECLARE GLOBAL VARIABLES

# --- DECLARE CLASSES

# --- DECLARE FUNCTIONS

# --- SETUP (runs once)
pygame.init()                                           # initialises pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))       # creates the screen
pygame.display.set_caption("Template")                  # sets the title bar text
clock = pygame.time.Clock()                             # initialised the pygame clock
running = True                                          # sets the running condition to true

# --- GAME LOOP (runs consistently)
while running:
    clock.tick(FPS)                                     # keeps the game running at the right speed
    
    # --- Event Handlers (check for different events and acts upon them)
    for event in pygame.event.get():                    # retrieves events from event record                
        # closing window event
        if event.type == pygame.QUIT:
            running = False                             # sets running condition to false, exiting the game loop

    # --- Update any changes in variables
    

    # --- Draw objects
    screen.fill(BLACK)
    
    
    # *after* drawing everything, flip the display (displays)
    pygame.display.flip()

pygame.quit()