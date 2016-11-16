from weapons_spells import *
from random import choice, randint
from unit import *
from metadata import *


class ReceiveTreasure:

    def __init__(self, recipient):
        self.recipient = recipient
        self.treasure = Treasure().pick_treasure()

    def assign_treasure_hero(self):
        if self.treasure[0] == "hp":
            print(HERO_FOUND_HEAL.format(hero=self.recipient,
                                         hp=self.treasure[1]))
            self.recipient.take_healing(self.treasure[1])
        elif self.treasure[0] == "mp":
            print(HERO_FOUND_MANA.format(hero=self.recipient,
                                         mp=self.treasure[1]))
            self.recipient.take_mana(self.treasure[1])
        elif self.treasure[0] == "weapons":
            print(HERO_FOUND_WEAPON.format(hero=self.recipient,
                                           weapon=self.treasure[1]))
            self.recipient.equip(self.treasure[1])
        else:
            self.recipient.learn(self.treasure[1])
            print(HERO_FOUND_SPELL.format(hero=self.recipient,
                                          spell=self.treasure[1]))


class Treasure:

    def __init__(self):
        self.treasures = self.create_treasures()

    def create_treasures(self):
        treasures = {}
        ilustrations = ["Rugged ", "Green ", "Big ", "Salty "]
        weapons = ["Axe", "Hammer", "Stick", "Mace"]
        spells = ["Fireball", "Exodia", "Avada Kedavra", "Expeliarmus"]
        treasures["hp"] = list(range(60))
        treasures["mp"] = list(range(40))
        treasures["weapons"] = [Weapon(choice(ilustrations) +
                                choice(weapons), randint(1, 35))
                                for i in range(4)]
        treasures["spells"] = [Spell(choice(spells),
                               randint(1, 55), randint(1, 25),
                               randint(1, 4)) for i in range(4)]
        return treasures

    def pick_treasure(self):
        tr_key = ["mp", "hp", "weapons", "spells"]
        item = randint(0, 3)
        return (tr_key[item], choice(self.treasures[tr_key[item]]))


def main():
    a = Treasure()
    print(a.pick_treasure())


if __name__ == "__main__":
    main()
