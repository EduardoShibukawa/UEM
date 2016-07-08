from unittest import TestCase

from Puzzle15.Puzzle15 import Puzzle15
from Puzzle15.Puzzle15AStarSolver import Puzzle15AStarSolver


class TestPuzzle15AStarSolver(TestCase):
    def __test_solve_x_moves__(self, g, m):
        s = Puzzle15('1 12 11 10 '
                     '2 13 0 9 '
                     '3 14 15 8 '
                     '4 5 6 7')
        solver = Puzzle15AStarSolver()
        self.assertEqual(solver.solve(s, g), m)

    def test_solve_case_1(self):
        self.__test_solve_x_moves__(
            Puzzle15("12 2 11 10 1 13 9 8 3 5 14 15 4 0 6 7 "),
            11)

    def test_solve_case_2(self):
        self.__test_solve_x_moves__(
            Puzzle15("2 1 9 11 12 13 10 0 3 14 15 8 4 5 6 7 "),
            11)

    def test_solve_case_3(self):
        self.__test_solve_x_moves__(
            Puzzle15("2 1 9 11 3 12 13 10 14 15 6 8 4 0 5 7 "),
            13)

    def test_solve_case_4(self):
        self.__test_solve_x_moves__(
            Puzzle15("1 12 10 13 2 6 11 0 3 14 15 9 4 5 7 8 "),
            15)

    def test_solve_case_5(self):
        self.__test_solve_x_moves__(
            Puzzle15("2 0 14 10 13 15 12 1 3 5 9 8 4 6 11 7 "),
            24)

    def test_solve_case_6(self):
        self.__test_solve_x_moves__(
            Puzzle15("1 14 11 10 2 6 12 8 3 0 15 9 5 4 7 13 "),
            34)

    def test_solve_case_7(self):
        self.__test_solve_x_moves__(
            Puzzle15("12 3 11 10 0 13 1 15 2 14 8 7 4 5 9 6 "),
            26)

    def test_solve_case_8(self):
        self.__test_solve_x_moves__(
            Puzzle15("2 12 15 11 4 3 6 10 1 0 7 9 5 13 14 8 "),
            26)

    def test_solve_case_9(self):
        self.__test_solve_x_moves__(
            Puzzle15("0 2 15 11 4 12 3 10 1 9 6 8 5 7 13 14 "),
            37)

    def test_solve_case_10(self):
        self.__test_solve_x_moves__(
            Puzzle15("4 2 15 11 1 12 3 10 9 7 6 8 5 0 13 14 "),
            39)
