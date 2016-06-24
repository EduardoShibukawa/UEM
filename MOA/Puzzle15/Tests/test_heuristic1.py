from unittest import TestCase
from Heuristic1 import Heuristic1
from Puzzle15 import *


class TestHeuristic1(TestCase):
    def test_8_unordered_values(self):
        p = Puzzle15('1 12 11 10 '
                     '2 13 0 9 '
                     '3 14 15 8 '
                     '4 5 6 7')
        p2 = Puzzle15('1 12 11 10 '
                      '3 14 15 8 '
                      '2 13 0 9 '
                      '4 5 6 7')

        h = Heuristic1(p, p2)
        self.assertEqual(h.calc(), 8)

    def test_no_unordered_values(self):
        p = Puzzle15('1 12 11 10 '
                     '2 13 0 9 '
                     '3 14 15 8 '
                     '4 5 6 7')
        p2 = Puzzle15('1 12 11 10 '
                      '2 13 0 9 '
                      '3 14 15 8 '
                      '4 5 6 7')

        h = Heuristic1(p, p2)
        self.assertEqual(h.calc(), 0)
