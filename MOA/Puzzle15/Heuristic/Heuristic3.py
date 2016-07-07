class Heuristic3:
    def __init__(self, current, goal):
        self._current = current
        self._goal = goal
        self.heuristic_value = -1

    @staticmethod
    def __calc_dist__(p1, p2):
        (x1, y1) = p1
        (x2, y2) = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def calc(self):
        if self.heuristic_value < 0:
            self.heuristic_value = 0
            if not hasattr(self._goal, 'dic_goal'):
                self._goal.dic_goal = {}

                for col in range(0, self._goal.size):
                    for lin in range(0, self._goal.size):
                        self._goal.dic_goal[self._goal.value[col][lin]] = (col, lin)

            for col in range(0, self._current.size):
                for lin in range(0, self._current.size):
                    self.heuristic_value += self.__calc_dist__(
                        self._goal.dic_goal[self._current.value[col][lin]],
                        (col, lin)
                    )

        return self.heuristic_value
