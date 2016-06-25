class Heuristic3:
    def __init__(self, current, goal):
        self.current = current
        self.goal = goal

    @staticmethod
    def __calc_dist__(p1, p2):
        (x1, y1) = p1
        (x2, y2) = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def calc(self):
        dic_goal = {}

        for col in range(0, self.goal.size):
            for lin in range(0, self.goal.size):
                dic_goal[self.goal.value[col][lin]] = (col, lin)

        distance_sum = 0
        for col in range(0, self.current.size):
            for lin in range(0, self.current.size):
                distance_sum += self.__calc_dist__(dic_goal[self.current.value[col][lin]], (col, lin))

        return distance_sum
