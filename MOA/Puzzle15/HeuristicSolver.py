class HeuristicSolver:
    def __init__(self):
        self._heuristics = []

    def add(self, heuristic):
        self._heuristics.append(heuristic)

    def clear(self):
        self._heuristics.clear()

    def solve(self):
        s = 0
        for h in self._heuristics:
            s = h.calc()
        return s
