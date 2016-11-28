from dungeon import *
from unit import *
from weapons_spells import *
from metadata import *


class GamingExperiance:

    def __init__(self):
        self.lvls = Levels()
        self.dung = Dungeon(self.lvls.levels.pop())
        self.begin_game()
        self.game_on = True
        self.play_it()

    def play_it(self):
        print(self.dung)
        while self.game_on:
            self.gaming_cycle()
            self.check_for_end()
            print(self.dung)

    def check_for_end(self):
        if self.dung.lvl_cleared:
            try:
                self.dung.format_map(self.lvls.levels.pop())
                print(self.dung)
                self.dung.h_pos = self.dung.get_spawn_pos()
                self.dung.spawn(self.dung.hero)
                self.dung.lvl_cleared = False
                print(NOT_LAST_LVL.format(hero=self.dung.hero))
            except IndexError:
                self.game_on = False
                print(LAST_LVL.format(hero=self.dung.hero))

    def begin_game(self):
        print(BEGIN_GAME)
        if input(CHOOSE_HERO) not in ["New Hero", "new"]:
            self.dung.spawn(Hero())
        else:
            h1 = input(HERO_NAME)
            h2 = input(HERO_TITLE)
            h3 = input(HERO_HP)
            h4 = input(HERO_MP)
            h5 = input(HERO_MANA_REGEN)
            self.dung.spawn(Hero(h1, h2, h3, h4, h5))

    def game_over(self):
        print(GAME_OVER.format(hero=self.dung.hero.__str__()))
        if input("Play again?") in ["y", "Y", "Yes"]:
            self.lvls = Levels()
            self.dung = Dungeon(self.lvls.levels.pop())
            return self.begin_game()
        self.set_game_status(False)

    def set_game_status(self, status):
        self.game_on = status

    def gaming_cycle(self):
        moves = ["down", "up", "left", "right"]
        user_inp = input("What is thy bidding my master? ")
        if user_inp in moves:
            self.dung.move_hero(user_inp)
            if not self.dung.hero.is_alive():
                self.game_over()
        elif user_inp in ["help", "-help"]:
            print(HELP_INFO)
        elif user_inp in ["exit", "exit()", "e", "E"]:
            self.game_on = False
        elif user_inp in ["Learn Spell", "Spell", "spell"]:
            self.dung.hero.receive_spell()
        elif user_inp in ["Equip Weapon", "Equip", "equip"]:
            self.dung.hero.receive_weapon()
        elif user_inp in ["Hero", "hero"]:
            print(HERO_INFO.format(hero=self.dung.hero,
                                   hp=self.dung.hero.get_health(),
                                   mp=self.dung.hero.get_mana()))
        else:
            print(COMAND_ERROR)


def main():
    pass


if __name__ == "__main__":
    main()
