class Heuristic1:
    def __init__(self, current, goal):
        self.current = current
        self.goal = goal

    def calc(self):
        count = 0
        for i in range(0, self.current.size):
            for j in range(0, self.current.size):
                if self.current.value[i][j] != self.goal.value[i][j]:
                    count += 1
        return count
