class Heuristic1:
    def __init__(self, current, goal):
        self._current = current
        self._goal = goal
        self.heuristic_value = -1

    def calc(self):
        if self.heuristic_value < 0:
            self.heuristic_value = 0
            for i in range(0, self._current.size):
                for j in range(0, self._current.size):
                    if self._current.value[i][j] != self._goal.value[i][j]:
                        self.heuristic_value += 1

        return self.heuristic_value
