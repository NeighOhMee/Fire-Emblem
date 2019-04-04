#imports
import random
import time

#classes
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

        
        #temporary
        self.hit_chance = hit_chance
        self.crit_chance = crit_chance
        
    def attack(self, other):
        '''
        initiates the attack sequence
        '''
        hit_chance = self.hit_chance
        crit_chance = self.crit_chance
        #take out the self.alive stuff later
        if self.weapon != None and self.alive and other.alive:
            if self.weapon.weapon_type == 'physical':    
                damage = (self.strength + self.weapon.mount) - other.defense
            elif self.weapon.weapon_type == 'magic':
                damage = (self.magic + self.weapon.mount) - other.resistance
            print('Hit Chance is {:.0f}%\nCrit Chance is {:.0f}%'.format(hit_chance * 100, crit_chance * 100), flush = True)
            print('{} attacks with the {}'.format(self.name, self.weapon.name), flush = True)
            
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
                
        else:
            print('{} has no weapon equiped'.format(self.name), flush = True)
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

class Weapon(object):
    def __init__(self, name, weapon_type, mount, crit_multiplier = 2):
        self.name = name
        self.weapon_type = weapon_type
        self.mount = mount
        self.crit_multiplier = crit_multiplier

#functions
def one_alive(L):
    '''
    Checks the list to see if only 1 character is alive
    '''
    alive = 0
    for person in L:
        if person.alive:
            alive += 1
    if alive == 1:
        return True
    return False

def remaining(points):
    print('{} points remaining'.format(points))
    
def add(phrase, points):
    '''
    adds points to a certain atribute and keeps the player from adding more points
    than they have
    '''
    while True:
        added = int(input(phrase))
        if added < 0:
            print('Points added must be positive or 0')
        elif points - added >= 0:
            return added
        else:
            print('Too many points added, try again')
        
def print2(string):
    '''
    prints a string in an old NES format
    '''
    for character in string:
        if character != '\n':
            print(character, end = '', flush = True)
            time.sleep(0.03)
        else:
            print(character, end = '', flush = True)
            
def level_up(character1):
    print('{} leveed up, 5 stat points gained and 10 percentage points gained')
    stat_points = 5
    percentage_points = 10 
    print('{} stat points\n{} percentage points'.format(stat_points, percentage_points))
    print(character1)
    #Stat additions
    character1.max_health, stat_points = add_attribute('health', character1, character1.max_health, stat_points)
    remaining(stat_points)
    character1.strength, stat_points = add_attribute('stregnth', character1, character1.strength, stat_points)
    remaining(stat_points)
    character1.magic, stat_points = add_attribute('magic', character1, character1.magic, stat_points)
    remaining(stat_points)
    character1.defense, stat_points = add_attribute('defense', character1, character1.defense, stat_points)
    remaining(stat_points)
    character1.resistance, stat_points = add_attribute('resistance', character1, character1.resistance, stat_points)
    print('you now have {} stat points in reserve'.format(stat_points))
    
    #Percentage additions
    
def add_attribute(attribute_name, character, attribute, points):
    '''
    returns a tupple of the new value for the attributes and total points
    '''
    change = add('How many points do you want to add to {}\'s {}? '.format(character.name, attribute_name), points)
    attribute += change
    points -= change
    return attribute, points

if __name__ == '__main__':
    win = True
    #Character creaation
    alm = Character( 20, 9, 1, 15, 4, 0, 'Alm', (0,0), .75, .10)
    mage = Character( 18, 1, 7, 8, 2, 7, 'Mage', (2,2), .80, .05)
    zombie = Character( 72, 15, 0, 10, 3, 0, 'Zombie', (0,0), .20, .1)
    
    #weapon initialization
    steel_sword = Weapon('steel sword', 'physical', 1)
    levin_sword = Weapon('levin sword','magic', 2)
    killing_edge = Weapon('killing edge', 'physical', 3, 4)
    fire = Weapon('fire', 'magic', 3)
    claws = Weapon('claws', 'physical', 5)
    weapons = [steel_sword, levin_sword, killing_edge, fire, claws]    
    
    #playable character
    points = 15
    percentage_points = 80
    print('Your first opponent')
    print(str(alm))
    print('You have {} stat points to allocate'.format(points))
    name = input('What is your characters name? ').strip()
    health = 15 + add('How many points do you want to add to {}\'s base health of 15? '.format(name), points)
    points -= health - 15
    remaining(points)
    strength = add('What is your {}\'s strength?(damage addition to physical weapons) '.format(name), points)
    points -= strength
    remaining(points)
    magic = add('What is your {}\'s magic?(damage addition to magic weapons) '.format(name), points)
    points -= magic
    remaining(points)
    defense = add('What is your characters\'s defense?(damage subtraction from physical attacks) ', points)
    points -= defense
    remaining(points)
    resistance = add('Resistance?(damage subtraction from magical attacks) ', points)
    points -= resistance
    print('You now have {} stat points in reserve'.format(points))
    
    print('You have {} percentage points to allocate to your hit chance and critical chance'.format(percentage_points))
    hit_chance = add('Hit chance in %? ', percentage_points)
    percentage_points -= hit_chance
    hit_chance /= 100
    crit_chance = add('Critical chance in %? ', percentage_points)
    percentage_points -= crit_chance
    crit_chance /= 100
    remaining(percentage_points)
    print('You have {} percentage points in reserve'.format(percentage_points))
    player_weapon = input('What weapon do you want?(steel sword, levin sword, killing edge, or fire) ').strip()
    
    character1 = Character(health, strength, magic, 0, defense, resistance, name, (0,0), hit_chance, crit_chance)
    
    for weapon in weapons:
        if weapon.name == player_weapon.lower():
            character1.equip(weapon)
    
    
    alm.equip(steel_sword)
    zombie.equip(claws)
    mage.equip(fire)
    
    #Main code
    print('')
    turns = 0
    print('Your first opponent is {}'.format(alm.name))
    while not one_alive([alm, character1]):
        turns += 1
        alm.attack(character1)
        time.sleep(4)
        if not character1.alive:
            break
        character1.attack(alm)
        time.sleep(4)
        
    if alm.alive:
        print('{} wins!'.format(alm.name))
        win = False
    else:
        print('{} wins!'.format(character1.name))

    print('{} turn(s)'.format(turns))
    
    if win == True:
        level_up(character1)
        
