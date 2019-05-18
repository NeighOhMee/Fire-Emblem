#test for making dialoglue/text boxes in a game

import pygame
from pygame_functions import *

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
gameDisplay = pygame.display.set_mode((800, 800))
gameDisplay.fill(black)
clock = pygame.time.Clock()

#main game loop
done = False
while not done:
	for event in pygame.event.get():
        	#cliking the quit button
            if event.type == pygame.QUIT:
                done = True
    
	
	#max characters is width/font size (18 characters)
	messageBox("Can I has a hamboorgar? Pleaseeeeeeeee!!!!", gameDisplay, 12)
	pygame.display.update()
	clock.tick(60)

pygame.quit()