# Pygame template - skeleton for a new pygame project

# --- IMPORT LIBRARIES
import pygame
import random


# --- DECLARE CONSTANTS
WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# --- DECLARE GLOBAL VARIABLES
bubbles = []

# --- DECLARE CLASSES
class Bubble:
    def __init__(self, bubbleX, bubbleY, bubbleR):
        self.bubbleX = bubbleX
        self.bubbleY = bubbleY
        self.bubbleR = bubbleR

    def show(self, surface):
        pygame.draw.circle(surface, WHITE)

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    
    # Event Handlers
    for event in pygame.event.get():                # record events                
        # check for different events and act upon them
        
        # closing window
        if event.type == pygame.QUIT:
            running = False

    # Update any changes in variables
    

    # Draw objects
    screen.fill(BLACK)
    
    
    # *after* drawing everything, flip the display (displays)
    pygame.display.flip()

pygame.quit()