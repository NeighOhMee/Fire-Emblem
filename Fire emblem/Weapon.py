'''
Contains the weapon class for the game
'''
class Weapon(object):
    def __init__(self, name, weapon_type, mount, crit_multiplier = 2):
        self.name = name
        self.weapon_type = weapon_type
        self.mount = mount
        self.crit_multiplier = crit_multiplier