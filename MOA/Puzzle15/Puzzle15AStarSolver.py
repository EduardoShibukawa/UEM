from HeuristicSolver import *
from Heuristic1 import Heuristic1
from Heuristic2 import Heuristic2
from PriorityQueue import *
from Puzzle15 import *


class Puzzle15State:
    def __init__(self, puzzle, moves):
        self.puzzle = puzzle
        self.children = []
        self.moves = moves

    def __str__(self):
        return str(self.puzzle)

    def __generate_child__(self, direction):
        new = Puzzle15State(Puzzle15(self.puzzle), self.moves + 1)
        new.puzzle.move(direction)
        self.children.append(new)

    def generate_children(self):
        if not self.children:
            for direction in Direction:
                if self.puzzle.can_move(direction):
                    self.__generate_child__(direction)


class Puzzle15AStarSolver:
    @staticmethod
    def __indexed__(value):
        return str(value)

    def __init__(self):
        self.moves = -1

    def solve(self, start, goal):
        heuristic_solver = HeuristicSolver()
        self.moves = -1
        current_cost = {}
        open_states = PriorityQueue()
        open_states.put(0, Puzzle15State(start, 0))
        while not open_states.empty():
            current = open_states.get()
            if str(current.puzzle) == str(goal):
                self.moves = current.moves
                break

            current.generate_children()
            for c in current.children:
                if self.__indexed__(c.puzzle) not in current_cost:
                    heuristic_solver.clear()
                    ##heuristic_solver.add(Heuristic1(c.puzzle, goal))
                    heuristic_solver.add(Heuristic2(c.puzzle))
                    current_cost[self.__indexed__(current)] = c.moves
                    open_states.put(heuristic_solver.solve() + c.moves, c)

        return self.moves
