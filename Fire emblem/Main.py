'''
Main file for the Fire Emblem game
'''

#imports
from Character import *
from Sprite import *
from Weapon import *
from pygame_functions import *
from settings import *
from os import path
import pygame
import time
from map import *

#functions
'''
def draw_grid():
	
	#Draws the game grid

	#vertical
	for i in range(0, width, tileSize):
		pygame.draw.line(gameDisplay, gray,(i,0), (i,width))
	#horizontal
	for i in range(0, height, tileSize):
		pygame.draw.line(gameDisplay, gray, (0,i), (height,i))
'''
def check_collisions(character, direction):
	'''
	keeps the user from moving into the same spot as an enemy
	returns
	'''
	if direction == "r":
		if current_character.sprite.x == 24 * tileSize:
			return False
		#checks collision with enemies
		for enemy in enemies:
			if (character.position[0] + 1, character.position[1]) == enemy.position:
				return False
		#checks collision with water
		for water in water_coord:
			if (character.position[0] + 1, character.position[1]) == water:
				return False
	if direction == "l":
		#checks edge of the screen
		if current_character.sprite.x == 0:
			return False
		for enemy in enemies:
			if (character.position[0] - 1, character.position[1]) == enemy.position:
				return False
		for water in water_coord:
			if (character.position[0] - 1, character.position[1]) == water:
				return False

	if direction == "u":
		if current_character.sprite.y == 0:
			return False
		for enemy in enemies:
			if (character.position[0] , character.position[1] - 1) == enemy.position:
				return False
		for water in water_coord:
			if (character.position[0] , character.position[1] - 1) == water:
				return False
	if direction == "d":
		if current_character.sprite.y == 24 * tileSize:
			return False
		for enemy in enemies:
			if (character.position[0] , character.position[1] + 1) == enemy.position:
				return False
		for water in water_coord:
			if (character.position[0] , character.position[1] + 1) == water:
				return False	

	return True
'''
def draw_map(map_array):
	
	#draws the main map
	
	
	gameDisplay.fill(white)
	draw_tiles(map_array)
	alm.sprite.show(gameDisplay)
	zombie.sprite.show(gameDisplay)
	draw_grid()

def load_map(water_coord):
	#map load
	#n^2 operation can I make it more efficient?
	mapFile = open("map1.txt")
	map_array = []
	#create map_array
	for row in mapFile:
		row = row.strip()
		row_array = []
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

def updateMapScreen():
	draw_map(map_array)
	pygame.display.update()
'''
#main code
'''
water_coord = []
map_array = load_map(water_coord)
'''


#color definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (211, 211, 211)

#pygame initialiization
'''
pygame.init()

width = 800
height = 800
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jubulumdum")
clock = pygame.time.Clock()
'''

'''
#character creation
alm = Character( 20, 9, 1, 15, 4, 0, 'Alm', (0,0), 1, .10, blue)
steel_sword = Weapon('steel sword', 'physical', 1)
alm.equip(steel_sword)
current_character = alm 

mage = Character( 18, 1, 7, 8, 2, 7, 'Mage', (2,2), .80, .05, blue)
fire = Weapon('fire', 'magic', 3)
mage.equip(fire)

#enemy creation
zombie = Character( 72, 15, 0, 10, 3, 0, 'Zombie', (7,8), .20, .1, red)
claws = Weapon('claws', 'physical', 5)
zombie.equip(claws)
enemies = [zombie]
'''
mov = 500
turn = "player"

done = False
while not done:
	#TODO: Make a better delay system instead of this
	time.sleep(.09)
	for event in pygame.event.get():
            #cliking the quit botton
            if event.type == pygame.QUIT:
                done = True
	
	if turn == "player":
	    #movement
		keys = pygame.key.get_pressed()
		if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and check_collisions(current_character,"l"):
			current_character.moveLeft()
			mov -= 1
		#TODO: Change border check to apply for any tile size/ combine 2 and 3 into one function
		if (keys[pygame.K_RIGHT] or keys[pygame.K_d])  and check_collisions(current_character, "r"):
			current_character.moveRight()
			mov -= 1
		if (keys[pygame.K_UP] or keys[pygame.K_w]) and check_collisions(current_character, "u"):
			current_character.moveUp()
			mov -= 1
		if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and check_collisions(current_character, "d"):
			current_character.moveDown()
			mov -= 1

		#end turn
		if(keys[pygame.K_RETURN]):
			mov = 0

		#attack(prototype version)
		if keys[pygame.K_z]:
			current_character.attack(zombie, gameDisplay)
	elif turn == "enemy":
		zombie.moveCloser(current_character)
		mov = 5
		draw_map(map_array, alm, zombie)
		pygame.display.update()
		message("Player Phase", gameDisplay)
		turn = "player"

	#checks to see if player turn is over
	if mov == 0:
		draw_map(map_array, alm, zombie)
		pygame.display.update()
		message("Enemy Phase", gameDisplay)
		turn = "enemy"
	


	#debugging
	if keys[pygame.K_SPACE]:
		print(current_character.name)
		print(current_character.position)
		print(turn)
	
	#update the dispaly
	draw_map(map_array, alm, zombie)
	pygame.display.update()
	clock.tick(60)
pygame.quit()

