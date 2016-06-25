class Heuristic2:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def __generate_puzzle_spiral_list__(self):
        lst = []
        c = ini = 0
        lim = self.puzzle.size - 1
        while c < self.puzzle.size * self.puzzle.size:
            for i in range(ini, lim + 1):
                lst.append(self.puzzle.value[i][ini])
                c += 1
            for i in range(ini + 1, lim + 1):
                lst.append(self.puzzle.value[lim][i])
                c += 1
            for i in range(lim-1, ini - 1, -1):
                lst.append(self.puzzle.value[i][lim])
                c += 1
            for i in range(lim-1, ini, -1):
                lst.append(self.puzzle.value[ini][i])
                c += 1

            ini += 1
            lim -= 1

        return lst

    def calc(self):
        l = self.__generate_puzzle_spiral_list__()

        count = 0
        b = 0
        for c in l:
            if b != 0:
                if (b != 15 and
                            c == 0):
                    count += 1
                elif (b + 1) != c:
                    count += 1
            b = c
        return count
