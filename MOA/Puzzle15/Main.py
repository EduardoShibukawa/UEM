import sys
import time
from functools import wraps
from Puzzle15.Puzzle15 import Puzzle15
from Puzzle15.Puzzle15AStarSolver import Puzzle15AStarSolver


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("Total time running %s: %s seconds" %
              (function.__name__, str(t1-t0)))
        return result
    return function_timer

#@profile
@fn_timer
def solve(str_puzzle):
    solver = Puzzle15AStarSolver()
    goal = Puzzle15('1 12 11 10 '
                    '2 13 0 9 '
                    '3 14 15 8 '
                    '4 5 6 7')
    start = Puzzle15(str_puzzle)
    print(solver.solve(start, goal))


def main():
    if len(sys.argv) > 1:
        str_puzzle = sys.argv[1]
    else:
        str_puzzle = input()

    print(str_puzzle)
    solve(str_puzzle)


if __name__ == '__main__':
    main()

