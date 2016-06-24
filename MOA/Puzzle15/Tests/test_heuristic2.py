from unittest import TestCase
from Heuristic2 import *
from Puzzle15 import Puzzle15


class TestHeuristic2(TestCase):
    def test_6_unordered_values(self):
        p = Puzzle15('12 1 2 3 '
                     '4 5 7 8 '
                     '0 9 10 11 '
                     '13 14 6 15')

        h = Heuristic2(p)
        self.assertEqual(h.calc(), 6)

    def test_no_unordered_values(self):
        p = Puzzle15('0 1 2 3 '
                     '4 5 6 7 '
                     '8 9 10 11 '
                     '12 13 14 15')

        h = Heuristic2(p)
        self.assertEqual(h.calc(), 0)
