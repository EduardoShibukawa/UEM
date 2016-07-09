from Heuristic.Heuristic1 import Heuristic1
from Heuristic.Heuristic2 import Heuristic2
from Heuristic.Heuristic3 import Heuristic3
from Heuristic.Heuristic4 import Heuristic4
from Heuristic.Heuristic5 import Heuristic5
from Utils.PriorityQueue import PriorityQueue
from Puzzle15.Puzzle15 import *


class Puzzle15State:
    def __lt__(self, other):
        return self.fn() < other.fn()

    def __init__(self, puzzle, moves):
        self.puzzle = puzzle
        self.children = set()
        self.moves = moves
        self.heuristic_value = 0

    def __str__(self):
        return str(self.puzzle)

    def __generate_child__(self, direction):
        new = Puzzle15State(Puzzle15(self.puzzle), self.moves + 1)
        new.puzzle.move(direction)
        self.children.add(new)

    def generate_children(self):
        if not self.children:
            for direction in Direction:
                if self.puzzle.can_move(direction):
                    self.__generate_child__(direction)

    def fn(self):
        return self.heuristic_value + self.moves


class Puzzle15AStarSolver:
    @staticmethod
    def __indexed__(value):
        return str(value)

    def __init__(self):
        self.moves = -1

    def solve(self, start, goal):
        closed_states = set()
        open_states = PriorityQueue()
        open_states.put(Puzzle15State(start, 0))
        self.moves = -1

        while not open_states.empty():
            current = open_states.get()

            if str(current.puzzle) == str(goal):
                self.moves = current.moves
                break

            closed_states.add(self.__indexed__(current))
            current.generate_children()
            for c in current.children:
                if self.__indexed__(c) not in closed_states:
                    #h1 = Heuristic1(c.puzzle, goal)
                    #h2 = Heuristic2(c.puzzle)
                    h3 = Heuristic3(c.puzzle, goal)
                    #h4 = Heuristic4(h1, h2, h3)
                    #h5 = Heuristic5(h1, h2, h3)

                    c.heuristic_value = h3.calc()
                    open_states.put(c)

        return self.moves
