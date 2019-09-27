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
from Zone import *

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
        self.zone = 0
        
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
            #message("Sample Text", gameDisplay)
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
                messageBox('Hit Chance is {:.0f}% \nCrit Chance is {:.0f}%'.format(hit_chance * 100, crit_chance * 100), gameDisplay)
                print('{} attacks with the {}'.format(self.name, self.weapon.name), flush = True)
                gameDisplay.fill(black)
                messageBox('{} attacks with the {}'.format(self.name, self.weapon.name), gameDisplay)
                
                if random.random() > hit_chance:
                    print('{} missed!'.format(self.name), flush = True)
                    gameDisplay.fill(black)
                    messageBox('{} missed!'.format(self.name),gameDisplay)
                else:
                    #Critial damage multiplier
                    if crit_chance > random.random():
                        damage *= self.weapon.crit_multiplier
                        print('CRITICAL!', flush = True)
                        gameDisplay.fill(black)
                        messageBox('CRITICAL!', gameDisplay)
                    other.current_health -= damage
                    print('{} did {} damage!'.format(self.name, damage), flush = True)
                    gameDisplay.fill(black)
                    messageBox('{} did {} damage!'.format(self.name, damage),gameDisplay)
                    other.health_check()
                    print('{}\'s health is now {}'.format(other.name, other.current_health), flush = True)
                    gameDisplay.fill(black)
                    messageBox('{}\'s health is now {}'.format(other.name, other.current_health),gameDisplay)
                    #checks if the character has no health
                    if other.current_health == 0:
                        print('{} has been slain!'.format(other.name), flush = True)
                        gameDisplay.fill(black)
                        messageBox('{} has been slain!'.format(other.name),gameDisplay)
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

    def zone_up(self): #Updates the character's zone to the one it's currently in
        for zone in zones:
            if zone.inzone(self.position):
                self.zone = zone
                break

    #movement funtions
    def moveLeft(self):
        self.position = (self.position[0] - 1, self.position[1])
        self.sprite.x -= tileSize
        self.zone_up()
    def moveRight(self):
        self.position = (self.position[0] + 1, self.position[1])
        self.sprite.x += tileSize
        self.zone_up()
    def moveUp(self):
        self.position = (self.position[0], self.position[1] - 1)
        self.sprite.y -= tileSize
        self.zone_up()
    def moveDown(self):
        self.position = (self.position[0], self.position[1] + 1)
        self.sprite.y += tileSize
        self.zone_up()

    def check_pathing(self, direction): #Same as check collisions but does not check enemies
        if direction == "r":
            if self.sprite.x == 24 * tileSize:
                return False
            #checks collision with water
            for water in water_coord:
                if (self.position[0] + 1, self.position[1]) == water:
                    return False
        if direction == "l":
            #checks edge of the screen
            if self.sprite.x == 0:
                return False
            for water in water_coord:
                if (self.position[0] - 1, self.position[1]) == water:
                    return False
        if direction == "u":
            if self.sprite.y == 0:
                return False
            for water in water_coord:
                if (self.position[0] , self.position[1] - 1) == water:
                    return False
        if direction == "d":
            if self.sprite.y == 24 * tileSize:
                return False
            for water in water_coord:
                if (self.position[0] , self.position[1] + 1) == water:
                    return False	
        return True

    def moveCloser(self, other):
        self.zone_up()
        print(self.zone)
        print(other.zone)
        if self.zone != other.zone: #When the zones are not the same instead path first to the other zone
            xDisp = other.zone.xa - self.position[0]
            yDisp = other.zone.ya - self.position[1]
        else:
            xDisp = other.position[0] - self.position[0]
            yDisp = other.position[1] - self.position[1]
        if not self.adjacent_to(other):
            #Advanced checking as to what moves are valid and where the pathing points to.
            #Ensures a move is always made and that a move in the furthest direction is made (if valid)
            if abs(xDisp) > abs(yDisp) and ((xDisp > 0 and self.check_pathing("r")) or (xDisp < 0 and self.check_pathing("l"))):
                if xDisp > 0 and self.check_pathing("r"):
                    self.moveRight()
                if xDisp < 0 and self.check_pathing("l"):
                    self.moveLeft()
            elif abs(yDisp) > abs(xDisp) and ((yDisp > 0 and self.check_pathing("d")) or (yDisp < 0 and self.check_pathing("u"))):
                if yDisp > 0 and self.check_pathing("d"):
                    self.moveDown()
                if yDisp < 0 and self.check_pathing("u"):
                    self.moveUp()
            elif xDisp > 0 and self.check_pathing("r"):
                self.moveRight()
            elif xDisp < 0 and self.check_pathing("l"):
                self.moveLeft()
            elif yDisp > 0 and self.check_pathing("d"):
                self.moveDown()
            elif yDisp < 0 and self.check_pathing("u"):
                self.moveUp()
            #updateMapScreen(self, other)
            #time.sleep(1)
            #mov -= 1
            return False
        else:
            return True


#character creation
alm = Character( 20, 9, 1, 15, 4, 0, 'Alm', (0,0), 1, .10, blue)
steel_sword = Weapon('steel sword', 'physical', 1)
alm.equip(steel_sword)
 
mage = Character( 18, 1, 7, 8, 2, 7, 'Mage', (2,2), .80, .05, red)
fire = Weapon('fire', 'magic', 3)
mage.equip(fire)

#enemy creation
zombie = Character( 72, 15, 0, 10, 3, 0, 'Zombie', (18,12), .20, .1, red)
claws = Weapon('claws', 'physical', 5)
zombie.equip(claws)
enemies = [zombie, mage]
allies = [alm]