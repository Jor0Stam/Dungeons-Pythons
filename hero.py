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
<<<<<<< HEAD
        self.weapon = 0
        self.spell = 0
=======
        self.weapon = None
        self.spell = None
        # self.attack = None
>>>>>>> 0746405e6ce7786ee49eadf6697d25edf6a82914
        self.alive = True

    def __eq__(self, other):
        return self.name == other.name and self.title == other.title and self.health == other.health and self.mana == self.mana and self.mana_regeneration_rate == other.mana_regeneration_rate

    def __hash__(self):
        return hash(self.hash())

    def __str__(self):
        return "{} the {}".format(self.name, self.title)

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
            return False

    def get_mana(self):
        if self.is_alive():
            return self.mana
        else:
            return False

    def can_cast(self, spell):
        if self.mana > spell.get_mana_spell():
            return True
        else:
            return False

    def take_damage(self, dmg):
        if float(self.health) - abs(dmg) <= 0:
            self.alive = False
            return False
        else:
            self.health = float(self.health) - dmg
            return True

    def take_healing(self, healing_points):
        if not self.is_alive:
            return False
        if self.health + healing_points > self.max_health:
            self.health = self.max_health
        else:
            self.health += healing_points
        return True

    def take_mana(self, mana):
        if not self.is_alive():
            return False
        if self.mana + mana > self.max_mana:
            self.mana = self.max_mana
        else:
            self.mana += mana
        return True

    def equip(self, weapon):
        self.weapon = weapon
        return True

    def learn(self, spell):
        self.spell = spell
        return True

    def attack(self, by):
        if self.weapon or self.spell is not None:
            if by == 'weapon':
                return self.weapon.damage
            if by == 'spell':
                return self.spell.damage
        else:
            return 0

    def receive_treasure(self, treasure):
        if treasure[1] == "mp":
            self.take_mana(treasure[0])
        if treasure[1] == "hp":
            self.take_healing(treasure[0])
        if isinstance(treasure[1], Weapon):
            self.equip(treasure[0])
        if isinstance(treasure[1], Spell):
            self.learn(treasure[0])


def main():
    pass


if __name__ == "__main__":
    main()
