from sys import argv


class Point_on_map:

    def __init__(self, content, coords):
        self.content = content
        self.coords = coords

    def __str__(self):
        return "{}".format(self.content)


class Dungeon:

    def __init__(self):
        self.dung = self.format_map()
        self.max_coords = (0, 0)

    def format_map(self):
        formated = "".join(open(argv[1], "r").readlines())
        row = 0
        for line in formated:
            col = 0
            print("LINE{}: {}".format(row, line.replace("\n", "")))
            for el in line.replace("\n", ""):
                formated.append(Point_on_map(el, (row, col)))
                col += 1
                row += 1
        self.max_coords = (row, col)
        return formated


def main():
    pass


if __name__ == "__main__":
    main()
