from metadata import *
from unit import *


class Fight:

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        self.mortal_combat(self.hero, self.enemy)

    def mortal_combat(self, hero, enemy):
        self.begin_fight()
        while self.hero.is_alive() and self.enemy.is_alive():
            self.hero_move()
            self.enemy_move()
        print(BATTLE_END.format(self.who_lost()))

    def who_lost(self):
        if self.hero.is_alive():
            return "Enemy"
        return "Hero"

    def begin_fight(self):
        print(INIT_FIGHT.format(h=self.hero, hp=self.hero.get_health(),
                                mp=self.hero.get_mana(),
                                eh=self.enemy.get_health(),
                                em=self.enemy.get_mana(),
                                ed=self.enemy.get_damage()))

    def hero_move(self):
        attacked_by = ""
        self.enemy.take_damage(self.hero.attack())
        attacked_by = Attack(self.hero).get_meaning()
        if attacked_by == "Spell":
            print(HERO_ATTACK_SPELL.format(hero=self.hero.__str__(),
                                           spell=self.hero.spell.name,
                                           dmg=self.hero.attack(),
                                           hp=self.enemy.get_health()))
        elif attacked_by == "Weapon":
            print(HERO_ATTACK_WEAPON.format(hero=self.hero.__str__(),
                                            weapon=self.hero.weapon.name,
                                            dmg=self.hero.attack(),
                                            hp=self.enemy.get_health()))
        else:
            print(HERO_NO_ATTACK.format(hero=self.hero.__str__()))

    def enemy_move(self):
        self.hero.take_damage(self.enemy.attack())
        print(ENEMY_ATTACK.format(hero=self.hero.__str__(),
                                  dmg=self.enemy.attack(),
                                  hp=self.hero.get_health()))


def main():
    pass


if __name__ == "__main__":
    main()
