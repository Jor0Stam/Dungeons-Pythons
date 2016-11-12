class Weapon:

    def __init__(self, name="Old pen", damage=1):
        self.name = name
        self.damage = damage

    def get_damage(self):
        return self.damage


class Spell(Weapon):

    def __init__(self, name="Fireball", damage=30, mana_cost=50, cast_range=2):
        super().__init__(name, damage)
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def get_damage(self):
        return self.damage

    def get_mana_spell(self):
        return self.mana_cost

    def get_cast_range(self):
        return self.cast_range


def main():
    pass


if __name__ == "__main__":
        main()
