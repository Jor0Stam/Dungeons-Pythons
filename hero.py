# from enemy import Enemy
from weapons_spells import *

class Hero:
    def __init__(self, name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.max_health = health
        self.max_mana = mana
        self.weapon = 0
        self.spell = 0
        self.attack = 0
        # self.alive = True

    def __eq__(self, other):
        return self.name == other.name and self.title == other.title and self.health == other.health and self.mana == self.mana and self.mana_regeneration_rate == other.mana_regeneration_rate

    def __hash__(self):
        return hash(self.hash())

    def known_as(self):
        return '{} the {}'.format(self.name, self.title)

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def get_health(self):
        if self.is_alive():
            return self.health
        else:
            return "Your hero is dead"

    def get_mana(self):
        if self.is_alive():
            return self.mana
        else:
            return "Your hero is dead"

    def can_cast(self):
        if self.mana > get_mana_spell(spell):
            return True
        else:
            return False

    def take_damage(self, damage_points):
        return self.health - damage_points

    def take_healing(self, healing_points):
        if not self.is_alive:
            return False
        if self.health + healing_points > self.max_health:
            self.health = self.max_health
        else:
            self.health += healing_points
        return True

    def take_mana(self, mana):
        if make_a_move():
            if self.mana + self.mana_regeneration_rate > self.max_mana:
                self.mana = self.max_mana
        if get_a_mana_potion(mana):
            if self.mana + mana > self.max_mana:
                self.mana = self.max_mana
        if self.mana < 0:
            return False

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by):
        if self.weapon or self.spell != 0:
            if by is 'weapon':
                self.attack = self.weapon
                return self.attack
            if by is 'spell':
                self.attack = self.spell
                return self.attack

