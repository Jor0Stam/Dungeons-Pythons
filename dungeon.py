from hero import Hero
from weapons_spells import *

import random
import sys


class Place_on_map:

    def __init__(self, tag, coords):
        self.tag = tag
        self.content = self.set_content(tag)
        self.coords = coords

    def __str__(self):
        return "{}".format(self.tag)

    def set_content(self, content):
        if content == ".":
            return "Path"
        elif content == "#":
            return "Obstacle"
        elif content == "S":
            return "SpawnPoint"
        elif content == "G":
            return "GateAway"
        elif content == "T":
            return "Treasure"
        elif content == "E":
            return "Enemy"
        elif content == "H":
            return "Hero"
        else:
            content = content

    def get_content(self):
        return self.content

    def get_coords(self):
        return self.coords


class Dungeon:

    def __init__(self):
        self.max_coords = (0, 0)
        self.h_pos = None
        self.hero = None
        self.map = self.format_map(sys.argv[1])
        self.treasures = {"mp": [20, 30, 45], "hp": [30, 50, 60],
                          "weapons": [Weapon("SWAGchain", 20), Weapon("motika", 1000)],
                          "spells": [Spell("DormamuICameToBargain", 40, 8, 2)]}

    def __str__(self):
        result = ""
        for row in range(self.max_coords[0]):
            for col in range(self.max_coords[1]):
                result += self.map[col + row * (self.max_coords[1])].__str__()
            result += "\n"

        return result

    def __repr__(self):
        result = ""
        for row in range(self.max_coords[0]):
            for col in range(self.max_coords[1]):
                result += self.map[col + row * (self.max_coords[1])].__str__()
            result += "\n"

        return result

    def format_map(self, map):
        formated_map = []
        with open(map, "r") as f:
            row = 0
            col = 0
            for line in f.readlines():
                col = 0
                print("LINE{}: {}".format(row, line.replace("\n", "")))
                for el in line.replace("\n", ""):
                    formated_map.append(Place_on_map(el, (row, col)))
                    col += 1
                row += 1
            self.max_coords = (row, col)
        return formated_map

    def get_map(self):
        return [el.__str__() for el in self.map]

    def spawn(self, hero):
        self.hero = hero
        self.h_pos = self.get_spawn()
        self.move_hero_to_hl()

    def get_spawn(self):
        for el in self.map:
            if el.get_content() == "SpawnPoint":
                return el.get_coords()
        return (0, 0)

    def set_hero_location(self, direct):
        directions = {"up": (-1, 0), "down": (1, 0),
                      "left": (0, -1), "right": (0, 1)}
        if self.check_new_position(directions[direct]):
            self.h_pos = (self.h_pos[0] + directions[direct]
                          [0], self.h_pos[1] + directions[direct][1])
            return True
        return False

    def check_new_position(self, direct):
        return self.check_borders(direct) and self.is_valid_move(direct)

    def is_valid_move(self, direct):
        new_row = self.h_pos[0] + direct[0]
        new_col = self.h_pos[1] + direct[1]
        if self.map[new_col + new_row * (self.max_coords[1])].tag is "#":
            return False
        return True

    def check_borders(self, direct):
        return self.h_pos[0] + direct[0] >= 0 \
            and self.h_pos[1] + direct[1] >= 0 \
            and self.h_pos[0] + direct[0] <= self.max_coords[0] \
            and self.h_pos[1] + direct[1] <= self.max_coords[1]

    def move_hero_to_hl(self):
        self.map[self.h_pos[1] + self.h_pos[0] *
                 (self.max_coords[1])] = Place_on_map("H", self.h_pos)

    def clear_old_pos(self, pos):
        self.map[pos[1] + pos[0] *
                 (self.max_coords[1])] = Place_on_map(".", pos)

    def move_hero(self, direction):
        temp = self.h_pos
        if self.set_hero_location(direction):
            self.move_hero_to_hl()
            self.clear_old_pos(temp)
            if self.is_treasure():
                self.pick_treasure()
        else:
            print("Invalid MOVE !")

    def pick_treasure(self):
        treasure = self.get_treasure()
        self.hero.receive_treasure(treasure)

    def get_treasure(self):
        tr_key = ["mp", "hp", "weapons", "spells"]
        item = random.randrange(0, 4)
        return (random.choice(self.treasures[tr_key[item]]), tr_key[item])

    def is_treasure(self):
        return self.map[self.h_pos[1] + self.h_pos[0] * self.max_coords[1]]


def main():
    John = Hero("JohnSnow", "TheNothingKnower", 150, 100, 3)
    d = Dungeon()
    d.spawn(John)
    print(d.__str__())
    d.move_hero("down")
    print(d.__str__())
    d.move_hero("down")
    print(d.__str__())
    d.move_hero("left")
    print(d.__str__())
    d.move_hero("down")
    d.move_hero("right")
    print(d.__str__())


if __name__ == "__main__":
    main()
