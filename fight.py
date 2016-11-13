from metadata import *


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
            print(self.hero.is_alive())
            print(self.enemy.is_alive())
        BATTLE_END.format(self.who_won())

    def begin_fight(self):
        print(INIT_FIGHT.format(h=self.hero, hp=self.hero.get_health(),
            mp=self.hero.get_mana(), eh=self.enemy.get_health(),
            em=self.enemy.get_mana(), ed=self.enemy.get_damage()))

    def who_won(self):
        if self.hero.is_alive():
            return "Enemy"
        return"Hero"

    def hero_move(self):
        self.enemy.take_damage(self.hero.attack())
        print("Hero attack:")
        print(self.hero.attack())

    def enemy_move(self):
        self.hero.take_damage(self.enemy.attack())
        print("Enemy attack:")
        print(self.enemy.attack())


def main():
    pass


if __name__ == "__main__":
    main()
