'''
contains my self made functions for pygame
'''
#imports
import pygame
import time
from settings import *

#functions
def message(text, gameDisplay):
    font = pygame.font.Font("freesansbold.ttf", 32)
    textRender = font.render(text, True, white)
    #mess around with the coordinates for the second parameter
    gameDisplay.blit(textRender, (0,0))
    pygame.display.update()
    time.sleep(2)