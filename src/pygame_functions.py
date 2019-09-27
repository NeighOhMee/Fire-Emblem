'''
contains my self made functions for pygame
'''
#imports
import pygame
import time
from settings import *

#CUR_PATH = os.path.dirname(__file__)
FONT_PATH = os.path.relpath('..\\fonts\\PressStart2P.ttf')
#functions
def message(text, gameDisplay):
    font = pygame.font.Font(FONT_PATH, 32)
    textRender = font.render(text, True, white)
    #mess around with the coordinates for the second parameter
    gameDisplay.blit(textRender, (100,600))
    pygame.display.update()
    time.sleep(2)

def messageBox(text,gameDisplay, fontSize=12):
	font = pygame.font.Font(FONT_PATH, fontSize)
	lineLength = 600
	pygame.draw.rect(gameDisplay,(255,0,0),[100,600,lineLength,64])
	characters_per_line = lineLength // fontSize
	lines = []
	#parse spaces string until the length is too long for the line
	stringList = text.split(" ")
	line = ""
	#print(characters_per_line)
	for string in stringList:
		if len(line) + 1 + len(string) < characters_per_line:
			line += " " + string
		else:
			lines.append(line)
			line = " " + string
	lines.append(line)
	
	y = 600
	for messageLine in lines:
		x = 100
		for letter in messageLine:
			textRender = font.render(letter, True, white)
			gameDisplay.blit(textRender, (x,y))
			x+= fontSize
			time.sleep(.09)
			pygame.display.update()
		y+= fontSize
	time.sleep(1)
	