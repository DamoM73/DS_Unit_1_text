# Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 600
HEIGHT = 400
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fibonacci Bubbles")
clock = pygame.time.Clock()

# initalize values
sum = 0
f1 = 0
f2 = 1
numberOfBubbles = 0
xCentre = 10
yCentre = 200

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    
    
    if numberOfBubbles <= 10000:       # if 14 bubbles have not been drawn, keep updating values
        sum = f1 + f2
        f2 = f1
        f1 = sum
        radius = sum
        numberOfBubbles += 1
        pygame.draw.circle(screen, WHITE, [200,200], 100, 0)
        print(f1, " ", f2)
    
    
    # Draw / render
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, WHITE, [100,100,100,100])
    
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()