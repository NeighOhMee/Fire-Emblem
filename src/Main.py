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
def check_collisions(character, direction):
	'''
	keeps the user from moving into the same spot as an enemy or ally
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



#main code
if __name__ == "__main__":
	mov = 500
	turn = "player"
	done = False
	current_character = alm
	#TODO: initialize zones somewhere...
	alm.zone_up()
	while not done:
		#TODO: Make a better delay system instead of this for key presses
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
			for enemy in enemies:
				enemyMov = 3
				while enemyMov!=0:
					if not enemy.moveCloser(current_character):
						enemyMov -= 1
					else:
						enemyMov = 0
					draw_map(map_array, allies, enemies)
					pygame.display.update()
					time.sleep(1)	
					
			mov = 5
			draw_map(map_array, allies, enemies)
			pygame.display.update()
			message("Player Phase", gameDisplay)
			turn = "player"

		#checks to see if player turn is over
		if mov == 0:
			draw_map(map_array, allies, enemies)
			pygame.display.update()
			message("Enemy Phase", gameDisplay)
			turn = "enemy"
		


		#debugging
		if keys[pygame.K_SPACE]:
			#print(current_character.name)
			#print(current_character.position)
			#print(turn)
			print(mov)
		
		#update the display
		#TODO: don't redraw the map every clock tick if it proves too wasteful
		draw_map(map_array, allies, enemies)
		pygame.display.update()
		clock.tick(60)
	pygame.quit()

