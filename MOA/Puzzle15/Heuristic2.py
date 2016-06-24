class Heuristic2:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def calc(self):
        count = 0
        b = 0
        for col in range(0, self.puzzle.size):
            for lin in range(0, self.puzzle.size):
                c = self.puzzle.value[col][lin]
                if b != 0:
                    if (b + 1) != c:
                        count += 1
                b = c

        return count
