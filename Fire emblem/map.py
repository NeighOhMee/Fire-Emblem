import pygame
from Sprite import *
from Weapon import *
from Zone import *
'''
contains the data and functions for the map
'''
def draw_grid():
	'''
	Draws the game grid
	'''
	#vertical
	for i in range(0, width, tileSize):
		pygame.draw.line(gameDisplay, gray,(i,0), (i,width))
	#horizontal
	for i in range(0, height, tileSize):
		pygame.draw.line(gameDisplay, gray, (0,i), (height,i))

def draw_map(map_array, character1, character2):
	'''
	draws the main map
	'''
	
	gameDisplay.fill(white)
	draw_tiles(map_array)
	character1.sprite.show(gameDisplay)
	character2.sprite.show(gameDisplay)
	draw_grid()

def load_map(water_coord, zones):
	#map load
	#n^2 operation can I make it more efficient?
	mapFile = open("map1.txt")
	map_array = []
	#create map_array
	for row in mapFile:
		row = row.strip()
		row_array = []
		if row[0] == "#": #First checks the line if it designates a zone
			#Zone line format is "#x1-x2,y1-y2" with x1 and y1 < x2 and y2 respectively
			dashx = row.find("-",1)
			dashy = row.find("-",dashx+1)
			sep = row.find(",")
			zones.append(Zone(int(row[1:dashx]), int(row[dashx+1:sep]), int(row[sep+1:dashy]), int(row[dashy+1:])))
		else:
			for tile in row:	
				row_array.append(tile)
			map_array.append(row_array)
	
	for i in range(len(map_array)):
		for j in range(len(map_array[0])):
			tile = map_array[i][j]
			if tile == "*":
				map_array[i][j] = Sprite((j, i),green)
			elif tile == "b":
				map_array[i][j] = Sprite((j, i), brown)
			elif tile == "w":
				map_array[i][j] = Sprite((j, i), water_blue)
				water_coord.append((j,i))
	
	
	return map_array

def draw_tiles(l):
	for row in l:
		for tile in row:
			tile.show(gameDisplay)

def updateMapScreen(character1, character2):
	draw_map(map_array, character1, character2)
	pygame.display.update()

pygame.init()

width = 800
height = 800
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jubulumdum")
clock = pygame.time.Clock()



#color definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (211, 211, 211)

water_coord = []
zones = []
map_array = load_map(water_coord, zones)