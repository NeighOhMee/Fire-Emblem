#test for making dialoglue/text boxes in a game

import pygame
from pygame_functions import *
#functions
def pollEvents():
	global DONE
	while True:
		for event in pygame.event.get():
	     		#cliking the quit button
	     		print("checking events")
	     		if event.type == pygame.QUIT:
	     			pygame.quit()
	     			sys.exit(0)
	     			done = True
def pollEvents2():
	global done
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
	         pygame.quit()
	         #sys.exit(0)
	         done = True
            


pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
gameDisplay = pygame.display.set_mode((800, 800))
gameDisplay.fill(black)
clock = pygame.time.Clock()

done = False
#main game loop
while not done:
	#max characters is width/font size (18 characters)
	messageBox("Hi my name is bob", gameDisplay, 12)
	#pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
	         done = True
	         pygame.quit()
	clock.tick(60)

