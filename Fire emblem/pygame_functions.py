'''
contains my self made functions for pygame
'''
#imports
import pygame
import time
from settings import *

#functions
def message(text, gameDisplay):
    font = pygame.font.Font("PressStart2P.ttf", 32)
    textRender = font.render(text, True, white)
    #mess around with the coordinates for the second parameter
    gameDisplay.blit(textRender, (100,600))
    pygame.display.update()
    #time.sleep(2)

def messageBox(text,gameDisplay, fontSize):
	font = pygame.font.Font("PressStart2P.ttf", fontSize)
	lineLength = 600
	pygame.draw.rect(gameDisplay,(255,0,0),[100,600,lineLength,64])
	characters_per_line = lineLength // fontSize
	lines = []
	#parse spaces in string until the length is too long for the line
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
	x = 600
	for messageLine in lines:
		textRender = font.render(messageLine, True, white)
		gameDisplay.blit(textRender, (100,x))
		x+= fontSize
	pygame.display.update()