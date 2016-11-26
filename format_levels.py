class Point_on_map:

    def __init__(self, content, coords):
        self.content = content
        self.coords = coords

    def __str__(self):
        return "{}".format(self.content)

    def __repr__(self):
        return "{}".format(self.content)

    def get_content(self):
        return self.content

    def get_coords(self):
        return self.coords


class Level:

    def __init__(self, raw_info):
        self.max_coords = (0, 0)
        self.content = self.format_map(raw_info)

    def format_map(self, content):
        formated = []
        row = col = 0
        for line in content:
            col = 0
            for el in line:
                formated.append(Point_on_map(el, (row, col)))
                col += 1
            row += 1
        self.max_coords = (row, col)
        # for line in open("level1.txt", "r").readlines():
        #     col = 0
        #     print("LINE{}: {}".format(row, line.replace("\n", "")))
        #     for el in line.replace("\n", ""):
        #         formated.append(Point_on_map(el, (row, col)))
        #         col += 1
        #     row += 1
        # self.max_coords = (row, col)
        return formated

    def get_max_coords(self):
        return self.max_coords


class Levels:

    def __init__(self):
        self.levels = self.get_lvls()
        self.level_num = self.count_lvls()

    def count_lvls(self):
        return len(self.levels)

    def get_lvls(self):
        lvls = []
        temp_lvl = []
        for line in open("levels.txt", "r").readlines():
            line = line.replace("\n", "")
            if self.is_int(line):
                lvls.append(Level(temp_lvl))
                temp_lvl = []
                continue
            temp_lvl.append(line)
        lvls.reverse()
        return lvls

    def is_int(self, el):
        try:
            int(el[0])
            return True
        except Exception:
            return False


def main():
    L = Levels()
    print(L.levels)


if __name__ == "__main__":
    main()
