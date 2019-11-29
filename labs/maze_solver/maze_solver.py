#!/usr/bin/env python3
import sys
from maze_support import Maze


class Solver:
    '''
    Will attempt to solve the maze.
    '''
    def __init__(self, maze):
        self.maze = maze
        self.start = maze.get_start()
        self.end = None
        self.curr_row, self.curr_col = self.start
        self.visited = set()
        self.seen = set()
        self.visited.add(self.start)
        self.seen.add(self.start)

    def search_quadrants(self):
        '''
        search_quadrants() -> NoneType

        Peers into the four coordinates around the current position.
        '''
        self.update_seen(self.curr_row + 1, self.curr_col)
        self.update_seen(self.curr_row - 1, self.curr_col)
        self.update_seen(self.curr_row, self.curr_col + 1)
        self.update_seen(self.curr_row, self.curr_col - 1)

    def update_seen(self, row, col):
        '''
        update_seen(int, int) -> NoneType

        Checks the position and updates seen if position is empty.
        '''
        value = self.maze.get_point(row, col)
        if value == ' ':
            self.seen.add((row, col))
        elif value == 'E':
            self.none((row, col))

    def __str__(self):
        min_row = min((row for row, col in self.seen))
        min_col = min((col for row, col in self.seen))
        max_row = max((row for row, col in self.seen))
        max_col = max((col for row, col in self.seen))
        print(min_row, max_row)
        print(min_col, max_col)
        visited = []

        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                if (row, col) in self.seen:
                    visited.append(".")
                else:
                    visited.append(" ")
            visited.append("\n")

        return ''.join(visited)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid usage:")
        print("\nmaze_solver.py MAZE")
        sys.exit(0)

    maze = Maze(sys.argv[1])
    if maze is None:
        print("Unable to load maze: {}".format(sys.argv[1]))
        sys.exit(0)

    print(maze)

    start = maze.get_start()
    solver = Solver(maze)
    solver.search_quadrants()
    print(solver)
