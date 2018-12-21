# Pygame template - skeleton for a new pygame project

# --- IMPORT LIBRARIES
import pygame
import random


# --- DECLARE CONSTANTS
# screen constants
WIDTH = 640                                             # Screen width
HEIGHT = 480                                            # Screen Height
FPS = 30                                                # Frames per second

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# --- DECLARE GLOBAL VARIABLES
bubbles = []                                            # array that will contain the bubble objects

# --- DECLARE CLASSES
class Bubble:                                           # class for each bubble object
    def __init__(self, x, y, radius, speed):
        self.x = x                          # the x position of the bubble
        self.y = y                          # the y position of the bubble
        self.radius = radius                          # the radius of the bubble
        self.speed = speed

    def show(self, surface):                            # draws the bubble object onto the surface
        pygame.draw.circle(surface, WHITE,(self.x, self.y), self.radius, 0)

# --- DECLARE FUNCTIONS

# --- SETUP (runs once)
pygame.init()                                           # initialises pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))       # creates the screen
pygame.display.set_caption("Bouncing Bubbles")          # sets the title bar text
clock = pygame.time.Clock()                             # initialised the pygame clock
running = True                                          # sets the running condition to true

# --- GAME LOOP (runs consistently)
while running:
    clock.tick(FPS)                                     # keeps the game running at the right speed
    
    # --- Event Handlers (check for different events and acts upon them)
    for event in pygame.event.get():                    # retrieves events from event record                
        
        if event.type == pygame.QUIT:                   # checks for closing window event
            running = False                             # sets running condition to false, exiting the game loop

        elif event.type == pygame.MOUSEBUTTONUP:        # checks for mouse click event
            mouseX = pygame.mouse.get_pos()[0]          # records mouse x value
            mouseY = pygame.mouse.get_pos()[1]          # record mouse y value
            bubbles.append(Bubble(mouseX,mouseY,25,10))    # create a bubble os radius 25 at the position of the mouse

    # --- Update any changes in variables
    for bubble in bubbles:                              # move each bubble object in the bubble array
        bubble.y += bubble.speed            # each bubble will move each loop at the speed
        if bubble.y + bubble.radius > HEIGHT or bubble.y - bubble.radius < 0:         # check if bubble is at edge screen
            bubble.speed *= -1
    

    # --- Draw objects
    screen.fill(BLACK)                                  # create a black background 
    
    for bubble in bubbles:                              # draw each bubble object in the bubble array
        bubble.show(screen)                             # each bubble's show method is called
    
    # *after* drawing everything, flip the display (displays)
    pygame.display.flip()

pygame.quit()