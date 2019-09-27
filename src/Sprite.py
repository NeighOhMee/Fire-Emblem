'''
creates a sprite object to display on the screen
'''
#imports
import pygame
from settings import *

class Sprite(object):
    def __init__(self, position, image):
        self.x = position[0] * tileSize
        self.y = position[1] * tileSize
        #self.image = pygame.image.load(image)
        self.image = pygame.Surface((tileSize, tileSize))
        self.image.fill(image)
        self.dx = 10
        self.dy = 0
        
    def show(self, gameDisplay):
        '''
        displays the sprite on the screen
        '''
        gameDisplay.blit(self.image, (self.x, self.y))

