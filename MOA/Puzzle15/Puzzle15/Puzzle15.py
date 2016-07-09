from enum import Enum
from array import *


class InvalidPuzzle15Move(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Direction(Enum):
        up = 1
        down = 2
        right = 3
        left = 4


class Puzzle15:
    def __init__(self, value):
        self.size = 4
        self.value = array('i', [])
        self._str_value = ""
        if type(value) is str:
            i = 0
            value = value.split(" ")
            for v in value:
                if v != '':
                    self.value.append(int(v))
                    self._str_value += v.zfill(2)
                    if int(v) == 0:
                        self.empty_pos = (i // 4, i % 4)
                    i += 1

        elif type(value) is Puzzle15:
            self.empty_pos = value.empty_pos[:]
            self.value = value.value[:]
            self._str_value = str(value)[:]

    def get_value(self, i, j):
        return self.value[(i * 4) + j]

    def valid_position(self, x, y):
        return (x < self.size) and (x >= 0) and (y < self.size) and (y >= 0)

    def can_move(self, direction):
        (col, line) = self.empty_pos

        if direction == Direction.up:
            col -= 1
        elif direction == Direction.down:
            col += 1
        elif direction == Direction.right:
            line += 1
        elif direction == Direction.left:
            line -= 1

        return self.valid_position(col, line)

    def move(self, direction):
        (col, line) = self.empty_pos

        if direction == Direction.up:
            col -= 1
        elif direction == Direction.down:
            col += 1
        elif direction == Direction.right:
            line += 1
        elif direction == Direction.left:
            line -= 1

        if not self.valid_position(col, line):
            raise InvalidPuzzle15Move('Movimento Invalido!')

        l = [self._str_value[i:i+2] for i in range(0, len(self._str_value), 2)]
        i_0 = l.index('00')
        i_v = l.index(str(self.get_value(col, line)).zfill(2))
        l[i_0], l[i_v] = l[i_v], l[i_0]
        self._str_value = "".join(l)

        self.value[self.empty_pos[0] * 4 + self.empty_pos[1]], self.value[col * 4 + line] \
            = self.value[col * 4 + line], self.value[self.empty_pos[0] * 4 + self.empty_pos[1]]
        self.empty_pos = (col, line)

    def __str__(self):
        return self._str_value


