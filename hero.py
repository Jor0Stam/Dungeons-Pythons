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
        self.weapon = None
        self.spell = None
        # self.attack = None
        self.alive = True

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
        if make_a_move():
            if self.mana + self.mana_regeneration_rate > self.max_mana:
                self.mana = self.max_mana
        if get_a_mana_potion(mana):
            if self.mana + mana > self.max_mana:
                self.mana = self.max_mana
                return True
        if self.mana < 0:
            return False

    def equip(self, weapon):
        self.weapon = weapon
        return True

    def learn(self, spell):
        self.spell = spell
        return True

    def attack(self, by):
        print("dww")
        if self.weapon or self.spell is not None:
            print("vlqzoh")
            if by == 'weapon':
                print("i tuka")
                self.attack = self.weapon.damage
                return self.attack
            if by == 'spell':
                print("i tam")
                self.attack = self.spell.damage
                return self.attack
        return 0


# def main():
#     # super_gosho = Hero(name="Gosho", title="Ubiec", health=100, mana=100, mana_regeneration_rate=2)
#     # captain_america = Hero(name="America", title="Captain", health=10, mana=10, mana_regeneration_rate=1)
#     # spell = Spell("Fireball", 30, 5, 2)
#     # captain_america.learn(spell)
#     # print(captain_america.attack('spell'))

# if __name__ == "__main__":
#     main()