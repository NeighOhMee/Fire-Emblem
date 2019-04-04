#test for making dialoglue/text boxes in a game

import pygame
from pygame_functions import *

white = (255, 255, 255)
gameDisplay = pygame.display.set_mode((800, 800))
gameDisplay.fill(white)

#main game loop
done = False
while not done:
	for event in pygame.event.get():
        	#cliking the quit button
            if event.type == pygame.QUIT:
                done = True

pygame.quit()