from weapons_spells import *


class Unit:

    def __init__(self, health, mana):
        self.max_hp = self.health = health
        self.max_mp = self.mana = mana
        self.status = True
        self.weapon = None
        self.spell = None

    def __eq__(self, other):
        return self.health == other.health and self.mana == self.mana

    def __hash__(self):
        return hash(self.hash())

    def is_alive(self):
        return self.status

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, heal):
        if self.is_alive():
            self.health += heal
            if self.health > self.max_hp:
                self.health = self.max_hp
            return True
        return False

    def take_mana(self, conjur):
        if self.is_alive():
            self.mana += conjur
            if self.mana > self.max_mp:
                self.mana = self.max_mp
            return True
        return False

    def can_cast(self):
        return self.spell

    def learn(self, spell):
        self.spell = spell

    def take_damage(self, dmg=0):
        if dmg is None:
            dmg = 0
        if float(self.health) - abs(dmg) <= 0:
            self.health = 0
            self.go_dead()
        else:
            if float(self.health) == float(dmg):
                self.go_dead()
            self.health = float(self.health) - dmg
        return self.is_alive()

    def go_dead(self):
        self.status = False

    def has_spell(self):
        return self.spell

    def equip(self, weapon):
        self.weapon = weapon

    def has_weapon(self):
        return self.weapon


class Attack():

    def __init__(self, attacker, by=None):
        self.meaning_of_attack = None
        self.attacker = attacker
        self.damage = self.estimate_attack()
        self.by = self.check_for_by(by)

    def get_meaning(self):
        return self.meaning_of_attack

    def get_attack(self):
        return self.damage

    def check_for_by(self, by):
        if not by:
            return None
        weapons = {"Weapon": self.check_weapon(), "Spell": self.check_spell()}
        self.set_damage(weapons[by])

    def estimate_attack(self):
        if (self.check_weapon(), self.check_spell()) == (0, 0):
            self.meaning_of_attack = "None"
            return 0
        weapons = {"Weapon": self.check_weapon(), "Spell": self.check_spell()}
        print(type(weapons["Weapon"]))
        print(type(weapons["Spell"]))
        if weapons["Weapon"] > weapons["Spell"]:
            self.meaning_of_attack = "Spell"
            return self.set_damage(attacker.weapon.get_damage())
        self.meaning_of_attack = "Weapon"
        return self.set_damage(attacker.spell.get_damage())

    def check_spell(self):
        if self.attacker.has_spell():
            return self.attacker.spell.get_damage()
        return 0

    def check_weapon(self):
        if self.attacker.has_weapon():
            return self.attacker.weapon.get_damage()
        return 0

    def set_damage(self, dmg):
        self.damage = dmg


class Hero(Unit):

    def __init__(self, name="HeMan", title="BiG",
                 health=100, mana=100, mana_regen=3):
        super().__init__(health, mana)
        self.name = name
        self.title = title
        self.mana_regen = mana_regen

    def __str__(self):
        return "{} the {}".format(self.name, self.title)

    def __repr__(self):
        return "{} the {}".format(self.name, self.title)

    def __eq__(self, other):
        return self.health == other.health and self.mana == self.mana \
            and self.name == other.name and self.title == other.title  \
            and self.mana_regen == other.mana_regen

    def __hash__(self):
            return hash(self.hash())

    def attack(self, by=0):
        if by:
            return Attack(self.hero, by).get_attack()
        return Attack(self).get_attack()

    def check_is_there(self, by):
        to_check = {"spell": self.spell, self.weapon: self.weapon}
        try:
            self.to_check[by].get_damage()
            return to_check[by].get_damage()
        except Exception:
            return 0

    def move_mana(self):
        super(Hero, self).take_mana(self.mana_regen)

    def receive_spell(self):
        name = input("Spell name: ")
        damage = input("Spell damage: ")
        mana = input("Spell mana: ")
        cast_range = input("Spell cast range: ")
        self.learn(Spell(name, damage, mana, cast_range))

    def receive_weapon(self):
        name = input("Weapon name: ")
        damage = input("Weapon damage: ")
        self.equip(Weapon(name, damage))


class Enemy(Unit):

    def __init__(self, health=20, mana=20, damage=20):
            super().__init__(health, mana)
            self.damage = damage

    def attack(self):
        if self.can_cast():
            if self.mana - self.spell.get_mana_spell() > 0:
                return self.check_for_weapon()
            else:
                self.mana -= self.spell.get_mana_spell()
                return self.spell.get_damage()
        elif self.has_weapon():
            return self.weapon.get_damage()
        else:
            return self.damage

    def get_damage(self):
        return self.damage

    def check_for_weapon(self):
        if self.weapon:
            return self.weapon.get_damage()
        return self.damage


def main():
    pass


if __name__ == "__main__":
        main()
