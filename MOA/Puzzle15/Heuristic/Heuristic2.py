class Heuristic2:
    def __init__(self, puzzle):
        self._puzzle = puzzle
        self.heuristic_value = -1

    def __generate_puzzle_spiral_list__(self):
        lst = []
        c = ini = 0
        lim = self._puzzle.size - 1
        while c < self._puzzle.size * self._puzzle.size:
            for i in range(ini, lim + 1):
                lst.append(self._puzzle.value[i][ini])
                c += 1
            for i in range(ini + 1, lim + 1):
                lst.append(self._puzzle.value[lim][i])
                c += 1
            for i in range(lim - 1, ini - 1, -1):
                lst.append(self._puzzle.value[i][lim])
                c += 1
            for i in range(lim - 1, ini, -1):
                lst.append(self._puzzle.value[ini][i])
                c += 1

            ini += 1
            lim -= 1

        return lst

    def calc(self):
        if self.heuristic_value < 0:
            self.heuristic_value = 0
            l = self.__generate_puzzle_spiral_list__()

            b = 0
            for c in l:
                if b != 0:
                    if (b != 15 and
                                c == 0):
                        self.heuristic_value += 1
                    elif (b + 1) != c:
                        self.heuristic_value += 1
                b = c

        return self.heuristic_value
