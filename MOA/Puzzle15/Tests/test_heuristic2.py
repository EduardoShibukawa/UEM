from unittest import TestCase
from Heuristic2 import *
from Puzzle15 import Puzzle15


class TestHeuristic2(TestCase):
    def test_6_unordered_values(self):
        p = Puzzle15('12 11 10 9 '
                     '1 13 15 0 '
                     '2 14 6 8 '
                     '3 4 5 7')

        h = Heuristic2(p)
        self.assertEqual(h.calc(), 6)

    def test_ordered_values(self):
        p = Puzzle15('0 11 10 9 '
                     '1 12 15 8 '
                     '2 13 14 7 '
                     '3 4 5 6')
        h = Heuristic2(p)
        self.assertEqual(h.calc(), 0)
