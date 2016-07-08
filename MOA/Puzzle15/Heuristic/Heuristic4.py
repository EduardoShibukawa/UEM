class Heuristic4:
    def __init__(self, h1, h2, h3):
        self.heuristic_value = -1
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3

        """
            self.p1 = 0.2
            self.p2 = 0.0
            self.p3 = 0.8
        """
        self.p1 = 0.05
        self.p2 = 0.05
        self.p3 = 0.9

    def calc(self):
        if self.heuristic_value < 0:
          self.heuristic_value = (self.p1 * self.h1.calc()) + (self.p2 * self.h2.calc()) + (self.p3 * self.h3.calc())

        return self.heuristic_value
