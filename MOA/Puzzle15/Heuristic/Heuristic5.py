class Heuristic5:
    def __init__(self, h1, h2, h3):
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3

    def calc(self):
        return max(self.h1.calc(), self.h2.calc(), self.h3.calc())
