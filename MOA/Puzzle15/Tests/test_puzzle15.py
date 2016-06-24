from unittest import TestCase
from Puzzle15 import *


class TestPuzzle15(TestCase):
    def test_create_puzzle(self):
        t = Puzzle15('1 12 11 10 '
                     '2 13 0 9 '
                     '3 14 15 8 '
                     '4 5 6 7')

        t2 = Puzzle15(t)
        self.assertEqual(str(t), str(t2))

    def test_move_down(self):
        t = Puzzle15('1 12 11 10 '
                     '2 13 0 9 '
                     '3 14 15 8 '
                     '4 5 6 7')

        tfinal = Puzzle15('1 12 11 10 '
                          '2 13 15 9 '
                          '3 14 6 8 '
                          '4 5 0 7')

        t.move(Direction.down)
        t.move(Direction.down)
        self.assertEqual(str(t), str(tfinal))
        self.assertRaises(InvalidPuzzle15Move, t.move, Direction.down)

