from unit import *
from weapons_spells import *


def main():
    jonkata = Hero("Jonkata", "Goyemiq", 15, 20, 3)
    print(jonkata.attack("spell"))


if __name__ == "__main__":
    main()
