'''
Contains the character class for the Fire Emblem Game
'''

#Imports
import random
import time
from Sprite import *
from settings import *
from pygame_functions import *
from map import *

#Classes
class Character(object):
    '''
    Holds all the data for a character
    '''
    def __init__(self, health, strength, magic, speed, defense, resistance, name, position, hit_chance, crit_chance, image = "pika.png"):
        #health is a tuple
        self.current_health = health
        self.max_health = health
        self.strength = strength
        self.magic = magic
        self.speed = speed
        self.defense = defense
        self.resistance = resistance
        self.name = name
        self.position = position
        self.weapon = None
        self.alive = True

        #sprite
        self.sprite = Sprite(position, image)
        
        #temporary
        self.hit_chance = 1
        self.crit_chance = 0
        
    def adjacent_to(self, other):
        if (self.position[0] + 1, self.position[1]) == other.position:
            return True
        elif(self.position[0] - 1, self.position[1]) == other.position:
            return True
        elif (self.position[0] , self.position[1] - 1) == other.position:
            return True
        elif (self.position[0] , self.position[1] + 1) == other.position:
            return True
        return False
    def attack(self, other, gameDisplay, depth = 1):
        '''
        initiates the attack sequence
        '''
        #can only attack if two charcters are next to each other and checks recursive depth
        if self.adjacent_to(other):
            gameDisplay.fill(black)
            pygame.display.update()
            message("Sample Text", gameDisplay)
            #time.sleep(5)
            hit_chance = self.hit_chance
            crit_chance = self.crit_chance
            #take out the self.alive stuff later
            if self.weapon != None and self.alive and other.alive:
                if self.weapon.weapon_type == 'physical':    
                    damage = (self.strength + self.weapon.mount) - other.defense
                elif self.weapon.weapon_type == 'magic':
                    damage = (self.magic + self.weapon.mount) - other.resistance
                print('Hit Chance is {:.0f}% \nCrit Chance is {:.0f}%'.format(hit_chance * 100, crit_chance * 100), flush = True)
                gameDisplay.fill(black)
                message('Hit Chance is {:.0f}% \nCrit Chance is {:.0f}%'.format(hit_chance * 100, crit_chance * 100), gameDisplay)
                print('{} attacks with the {}'.format(self.name, self.weapon.name), flush = True)
                gameDisplay.fill(black)
                message('{} attacks with the {}'.format(self.name, self.weapon.name), gameDisplay)
                
                if random.random() > hit_chance:
                    print('{} missed!'.format(self.name), flush = True)
                else:
                    #Critial damage multiplier
                    if crit_chance > random.random():
                        damage *= self.weapon.crit_multiplier
                        print('CRITICAL!', flush = True)
                    other.current_health -= damage
                    print('{} did {} damage!'.format(self.name, damage), flush = True)
                    other.health_check()
                    print('{}\'s health is now {}'.format(other.name, other.current_health), flush = True)
                    #checks if the character has no health
                    if other.current_health == 0:
                        print('{} has been slain!'.format(other.name), flush = True)
                    #enemy gets to attack next
                    elif depth != 2:
                        print('')
                        print("in the loop")
                        other.attack(self, gameDisplay, depth + 1)
                        #can attack again if speed is 5 greater than the enemy's
                        #TODO: create a condition where the enemy can also attack twice
                        if self.speed - other.speed >= 5:
                            self.attack(other, gameDisplay, 2)
                    
                    '''
                    if self.speed - other.speed >= 5:
                        self.attack(other, 2)
                    '''
            print('', flush = True)

    
    def health_check(self):
        '''
        checks the health of a character and keeps it from falling below 0
        '''
        if self.current_health <= 0:
            self.current_health = 0
            self.alive = False
    
    def equip(self, weapon):
        '''
        lets a character equip a weapon
        '''
        self.weapon = weapon
        
    def __str__(self):
        '''
        creates a string for the character stats
        '''
        s = '{}\nHealth: {}\nStrength: {}\nMagic: {}\nDefense: {}\nResistance: {}\nHit Chance: {}%\nCritical Chance: {}%'\
              .format(self.name, self.max_health, self.strength, self.magic, self.defense, self.resistance, self.hit_chance * 100, self.crit_chance * 100)
        return s

    def heal(self, amount):
        '''
        heals the character a specified amount
        '''
        #caps at max health
        if (self.max_health - self.current_health) < amount:
            self.current_health = self.max_health
        #condition for healing all heath
        elif amount == -1:
            self.current_health = self.max_health
        else:
            self.current_health += amount


    #movement funtions
    def moveLeft(self):
        self.position = (self.position[0] - 1, self.position[1])
        self.sprite.x -= tileSize
    def moveRight(self):
        self.position = (self.position[0] + 1, self.position[1])
        self.sprite.x += tileSize
    def moveUp(self):
        self.position = (self.position[0], self.position[1] - 1)
        self.sprite.y -= tileSize
    def moveDown(self):
        self.position = (self.position[0], self.position[1] + 1)
        self.sprite.y += tileSize

    def moveCloser(self, other):
        mov = 3
        while(mov !=0):
            xDisp = other.position[0] - self.position[0]
            yDisp = other.position[1] - self.position[1]
            if not self.adjacent_to(other):
                if abs(xDisp) > abs(yDisp):
                    if xDisp > 0:
                        self.moveRight()
                    if xDisp < 0:
                        self.moveLeft()
                else:
                    if yDisp > 0:
                        self.moveDown()
                    elif yDisp < 0:
                        self.moveUp()
                updateMapScreen(self, other)
                time.sleep(1)
                mov -= 1
            else:
                break


#character creation
alm = Character( 20, 9, 1, 15, 4, 0, 'Alm', (0,0), 1, .10, blue)
steel_sword = Weapon('steel sword', 'physical', 1)
alm.equip(steel_sword)
current_character = alm 

mage = Character( 18, 1, 7, 8, 2, 7, 'Mage', (2,2), .80, .05, blue)
fire = Weapon('fire', 'magic', 3)
mage.equip(fire)

#enemy creation
zombie = Character( 72, 15, 0, 10, 3, 0, 'Zombie', (18,12), .20, .1, red)
claws = Weapon('claws', 'physical', 5)
zombie.equip(claws)
enemies = [zombie]