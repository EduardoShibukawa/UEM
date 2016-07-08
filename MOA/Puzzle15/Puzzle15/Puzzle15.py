from enum import Enum
import copy


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
        self.value = []
        self._str_value = ""
        if type(value) is str:
            value = value.split(" ")
            list(filter(''.__ne__, value))
            for i in range(0, self.size):
                self.value.append([])
                for j in range(0, self.size):
                    self.value[i].append(int(value[(i * 4) + j]))
                    self._str_value += value[(i * 4) + j] + " "
                    if int(value[(i*4) + j]) == 0:
                        self.empty_pos = (i, j)
        elif type(value) is Puzzle15:
            self.empty_pos = value.empty_pos
            for i in range(0, self.size):
                self.value.append([])
                for j in range(0, self.size):
                    self.value[i].append(value.value[i][j])
                    self._str_value += str(value.value[i][j]) + " "

    def valid_position(self, x, y):
        return (x < self.size) \
               and (x >= 0) \
               and (y < self.size) \
               and (y >= 0)

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

        if self._str_value != '':
            l = self._str_value.split(" ")
            i_0 = l.index('0')
            i_v = l.index(str(self.value[col][line]))
            l[i_0], l[i_v] = l[i_v], l[i_0]
            self._str_value = " ".join(l)

        self.value[self.empty_pos[0]][self.empty_pos[1]], self.value[col][line] \
            = self.value[col][line], self.value[self.empty_pos[0]][self.empty_pos[1]]
        self.empty_pos = (col, line)

    def __to_str__(self):
        return "".join(
            str(self.value[x][y]) + " "
            for x in range(0, self.size)
            for y in range(0, self.size)
        )

    def __str__(self):
        if self._str_value == '':
            self._str_value = self.__to_str__()

        return self._str_value


