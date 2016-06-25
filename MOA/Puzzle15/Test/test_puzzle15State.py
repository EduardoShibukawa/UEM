from unittest import TestCase

from Puzzle15.Puzzle15 import *
from Puzzle15.Puzzle15AStarSolver import Puzzle15State


class TestPuzzle15State(TestCase):
    def test_generate_4_children(self):
        s = Puzzle15State(Puzzle15('1 12 11 10 '
                                   '2 13 0 9 '
                                   '3 14 15 8 '
                                   '4 5 6 7'), 0)
        s.generate_children()
        self.assertEqual(len(s.children), 4)
        self.assertEqual(s.children[0].moves, 1)

    def test_generate_2_children(self):
        s = Puzzle15State(Puzzle15('1 12 10 0 '
                                   '2 13 11 9 '
                                   '3 14 15 8 '
                                   '4 5 6 7'), 1)
        s.generate_children()
        self.assertEqual(len(s.children), 2)
        self.assertEqual(s.children[0].moves, 2)
