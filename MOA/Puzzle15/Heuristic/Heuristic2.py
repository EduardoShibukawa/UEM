class Heuristic2:
    def __init__(self, puzzle):
        self._puzzle = puzzle
        self.heuristic_value = -1

    def __gambis__(self, b, c):
        if b != 0:
            if (b != 15 and
                        c == 0):
                self.heuristic_value += 1
            elif (b + 1) != c:
                self.heuristic_value += 1

    def calc(self):
        if self.heuristic_value < 0:
            self.heuristic_value = 0
            b = 0
            c = ini = 0
            lim = self._puzzle.size - 1
            while c < self._puzzle.size * self._puzzle.size:
                for i in range(ini, lim + 1):
                    x = self._puzzle.get_value(i, ini)
                    self.__gambis__(b, x)
                    c += 1
                    b = x
                for i in range(ini + 1, lim + 1):
                    x = self._puzzle.get_value(lim, i)
                    self.__gambis__(b, x)
                    c += 1
                    b = x
                for i in range(lim - 1, ini - 1, -1):
                    x = self._puzzle.get_value(i, lim)
                    self.__gambis__(b, x)
                    c += 1
                    b = x
                for i in range(lim - 1, ini, -1):
                    x = self._puzzle.get_value(ini, i)
                    self.__gambis__(b, x)
                    c += 1
                    b = x

                ini += 1
                lim -= 1

        return self.heuristic_value
