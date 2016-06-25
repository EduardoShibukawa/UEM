from unittest import TestCase
from Puzzle15 import Puzzle15
from Puzzle15AStarSolver import Puzzle15AStarSolver


class TestPuzzle15AStarSolver(TestCase):
    def __test_solve_x_moves__(self, g, m):
        s = Puzzle15('1 12 11 10 '
                     '2 13 0 9 '
                     '3 14 15 8 '
                     '4 5 6 7')
        solver = Puzzle15AStarSolver()
        self.assertEqual(solver.solve(s, g), m)

    def test_solve_6_moves(self):
        self.__test_solve_x_moves__(
            Puzzle15('1 12 11 10 '
                     '0 13 15 9 '
                     '2 14 6 8 '
                     '3 4 5 7'),
            6)

    def test_solve_11_moves(self):
        self.__test_solve_x_moves__(
            Puzzle15('12 11 10 9 '
                     '1 13 15 0 '
                     '2 14 6 8 '
                     '3 4 5 7'),
            11)

    def test_solve_7_moves(self):
        self.__test_solve_x_moves__(
            Puzzle15('1 12 0 11 '
                     '2 13 15 10 '
                     '3 14 6 9 '
                     '4 5 7 8'),
            7)

    def test_solve_15_moves(self):
        self.__test_solve_x_moves__(
            Puzzle15('2 1 12 11 '
                     '3 0 15 10 '
                     '4 13 6 9 '
                     '5 14 7 8'),
            15)

    def test_solve_20_moves(self):
        self.__test_solve_x_moves__(
            Puzzle15('2 1 12 11 '
                     '3 15 6 10 '
                     '4 0 7 9 '
                     '5 13 14 8'),
            20)

    def test_solve_9_moves(self):
        s = Puzzle15("2 3 4 0 "
                     "1 5 7 8 "
                     "9 6 10 12 "
                     "13 14 11 15")
        g = Puzzle15("1 2 3 4 "
                     "5 6 7 8 "
                     "9 10 11 12 "
                     "13 14 15 0")

        solver = Puzzle15AStarSolver()
        self.assertEqual(solver.solve(s, g), 9)

    def test_solve_62_moves(self):
        self.__test_solve_x_moves__(
            Puzzle15("2 3 4 0 "
                     "1 5 7 8 "
                     "9 6 10 12 "
                     "13 14 11 15"),
            62)
