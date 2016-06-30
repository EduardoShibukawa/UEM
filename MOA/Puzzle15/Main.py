from Puzzle15.Puzzle15 import Puzzle15
from Puzzle15.Puzzle15AStarSolver import Puzzle15AStarSolver

def main():
    solver = Puzzle15AStarSolver()
    goal = Puzzle15('1 12 11 10 '
                    '2 13 0 9 '
                    '3 14 15 8 '
                    '4 5 6 7')
    str_puzzle = input()
    start = Puzzle15(str_puzzle)
    print(solver.solve(start, goal))


if __name__ == '__main__':
    main()

