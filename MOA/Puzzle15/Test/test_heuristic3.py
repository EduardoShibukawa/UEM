from unittest import TestCase

from Heuristic.Heuristic3 import Heuristic3
from Puzzle15.Puzzle15 import Puzzle15


class TestHeuristic3(TestCase):
    def __test_x_unordered_values__(self, p2, x):
        p = Puzzle15('1 12 11 10 '
                     '2 13 0 9 '
                     '3 14 15 8 '
                     '4 5 6 7')

        h = Heuristic3(p, p2)
        self.assertEqual(h.calc(), x)

    def test_12_unordered_values(self):
        self.__test_x_unordered_values__(
            Puzzle15('7 12 11 10 '
                     '2 13 0 9 '
                     '3 14 15 8 '
                     '4 5 6 1'),
            12
        )

    def test_8_unordered_values(self):
        self.__test_x_unordered_values__(
            Puzzle15('1 12 11 10 '
                     '3 14 15 8 '
                     '2 13 0 9 '
                     '4 5 6 7'),
            8
        )

    def test_no_unordered_values(self):
        self.__test_x_unordered_values__(
            Puzzle15('1 12 11 10 '
                     '2 13 0 9 '
                     '3 14 15 8 '
                     '4 5 6 7'),
            0
        )
