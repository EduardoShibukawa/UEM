class Heuristic1:
    def __init__(self, current, goal):
        self._current = current
        self._goal = goal
        self.heuristic_value = -1

    def calc(self):
        if self.heuristic_value < 0:
            self.heuristic_value = 0
            for i in range(0, self._current.size * self._current.size):
                    if self._current.get_value(i // 4, i % 4) != self._goal.get_value(i // 4, i % 4):
                        self.heuristic_value += 1

        return self.heuristic_value
