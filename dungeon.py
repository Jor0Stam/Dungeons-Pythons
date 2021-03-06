from fight import *
from unit import *
from treasure import ReceiveTreasure
from metadata import *
from format_levels import *


# class Point_on_map:

#     def __init__(self, content, coords):
#         self.content = content
#         self.coords = coords

#     def __str__(self):
#         return "{}".format(self.content)

#     def get_content(self):
#         return self.content

#     def get_coords(self):
#         return self.coords


class Dungeon:

    def __init__(self, lvl):
        self.max_coords = lvl.get_max_coords()
        self.dung = lvl.content
        self.h_pos = self.get_spawn_pos()
        self.hero = None
        self.enemy = Enemy(50, 30, 15)
        self.hero_died = False
        self.lvl_cleared = False

    def __str__(self):
        result = ""
        for row in range(self.max_coords[0]):
            for col in range(self.max_coords[1]):
                result += self.dung[col + row * (self.max_coords[1])].__str__()
            result += "\n"

        return result

    def __repr__(self):
        result = ""
        for row in range(self.max_coords[0]):
            for col in range(self.max_coords[1]):
                result += self.dung[col + row * (self.max_coords[1])].__str__()
            result += "\n"

        return result

    def format_map(self, lvl_map):
        self.dung = lvl_map.content

    def get_map(self):
        return self.dung

    def spawn(self, hero):
        self.hero = hero
        self.hero_status = True
        self.h_pos = self.get_spawn_pos()
        self.move_hero_to_hl()

    def get_spawn_pos(self):
        for el in self.dung:
            if el.get_content() == "S":
                return el.get_coords()

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
        if self.dung[new_col + new_row *
                     (self.max_coords[1])].get_content() is "#":
            return False
        return True

    def check_borders(self, direct):
        return self.h_pos[0] + direct[0] >= 0 \
            and self.h_pos[1] + direct[1] >= 0 \
            and self.h_pos[0] + direct[0] <= self.max_coords[0] \
            and self.h_pos[1] + direct[1] <= self.max_coords[1]

    def move_hero_to_hl(self):
        if self.is_something("E"):
            Fight(self.hero, self.enemy)
        if self.is_something("T"):
            ReceiveTreasure(self.hero).assign_treasure_hero()
        if self.is_something("G"):
            self.next_lvl()
        self.dung[self.h_pos[1] + self.h_pos[0] *
                  (self.max_coords[1])] = Point_on_map("H", self.h_pos)

    def next_lvl(self):
        self.lvl_cleared = True

    def is_something(self, content):
        # print(self.dung)
        return self.dung[self.h_pos[1] +
                         self.h_pos[0] *
                         self.max_coords[1]].get_content() == content

    def clear_old_pos(self, pos):
        self.dung[pos[1] + pos[0] *
                  (self.max_coords[1])] = Point_on_map(".", pos)

    def move_hero(self, direction):
        temp = self.h_pos
        if self.set_hero_location(direction):
            self.move_hero_to_hl()
            self.clear_old_pos(temp)
            self.hero.move_mana()
        else:
            print("Invalid MOVE !")


def main():
    pass


if __name__ == "__main__":
    main()
