from unittest import TestCase

from Puzzle15.Puzzle15 import Puzzle15
from Puzzle15.Puzzle15AStarSolver import Puzzle15State
from Utils.PriorityQueue import *


class TestPriorityQueue(TestCase):
    def test_put_3_elements(self):
        q = PriorityQueue()
        q.put(2, Puzzle15State(Puzzle15('1 12 11 10 '
                                        '2 13 0 9 '
                                        '3 14 15 8 '
                                        '4 5 6 7'), 2))
        q.put(1, Puzzle15State(Puzzle15('1 12 11 10 '
                                        '2 13 0 9 '
                                        '3 14 15 8 '
                                        '4 5 6 7'), 1))
        q.put(1, Puzzle15State(Puzzle15('1 12 10 11 '
                                        '2 13 0 9 '
                                        '3 14 15 8 '
                                        '4 5 6 7'), 1))
        q.put(0, Puzzle15State(Puzzle15('1 12 10 11 '
                                        '2 13 0 9 '
                                        '3 14 15 8 '
                                        '4 5 6 7'), 0))
        self.assertEqual(q.get().moves, 0)
        self.assertEqual(q.get().moves, 1)
        self.assertEqual(q.get().moves, 1)
        self.assertEqual(q.get().moves, 2)
