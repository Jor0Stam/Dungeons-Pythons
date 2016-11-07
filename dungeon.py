import sys


class Place_on_map:

    def __init__(self, content, coords):
        self.content = self.get_content(content)
        self.coords = coords

    def set_content(self, content):
        if content == ".":
            return "path"
        elif content == "#":
            return "obstacle"
        elif content == "S":
            return "SpawnPoint"
        elif content == "G":
            return "GateAway"
        elif content == "T":
            return "Treasure"
        else:
            return "Enemy"


class Dungeon:

    def __init__(self):
        self.map = sys.argv[1]
        self.map = self.format_map(self.map)

    def format_map(self, map):
        formated_map = []
        with open(map, "r") as f:
            for line, row in zip(f.readlines(), range(len(f.readline))):
                for el, col in zip(line, range(len(line))):
                    formated_map.append(Place_on_map(el), (row, col))

        return formated_map

    def spawn(self, hero):
        pass

    def print_map(self):
        print(self.map)

    def move_hero(self, direction):
        pass
