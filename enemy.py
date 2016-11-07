class Enemy:

    def __init__(self, health=100, mana=100, damage=20):
        self.health = health
        self.mana = mana
        self.damage = damage
        self.alive = True
        self.max_hlth = health
        self.max_mana = mana
        self.weapon = None
        self.spell = None

    def __eq__(self, other):
        return self.health == other.health and self.damage == other.damage and self.mana == self.mana

    def __hash__(self):
        return hash(self.hash())

    def is_alive(self):
        if self.alive:
            return True
        else:
            return False

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, heal):
        if self.is_alive():
            self.health += heal
            if self.health > self.max_hlth:
                self.health = self.max_hlth
            return True
        else:
            return False

    def take_mana(self, conjur):
        self.mana += conjur
        if self.mana > self.max_mana:
            self.mana = self.max_mana
            return True
        else:
            return False

    def can_cast(self, spell):
        return spell == self.spell

    def take_damage(self, dmg):
        if float(self.health) - abs(dmg) <= 0:
            self.alive = False
            return False
        else:
            self.health = float(self.health) - dmg
            return True

    def has_spell(self):
        return self.spell

    def has_weapon(self):
        return self.weapon

    def attack(self):
        if self.has_spell():
            return self.spell.get_damage()
        elif self.has_weapon():
            return self.weapon.get_damage()
        else:
            return self.damage

    def equip(self, weapon):
        self.weapon = weapon
