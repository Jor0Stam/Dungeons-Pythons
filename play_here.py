from unit import *
from weapons_spells import *
from dungeon import *


def main():
    jonkata = Hero("Jonkata", "Goyemiq", 15, 20, 3)
    d = Dungeon()
    d.spawn(jonkata)
    jonkata.learn(Spell())
    d.move_hero("down")
    d.move_hero("down")
    print(d)
    # print(jonkata.attack("spell"))


if __name__ == "__main__":
    main()
