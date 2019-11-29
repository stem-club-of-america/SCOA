#!/usr/bin/env python3
import time
import os
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
        self.curr_pos = self.start
        self.visited = set()
        self.seen = set()
        self.path = [self.start]
        self.visited.add(self.start)
        self.seen.add(self.start)
        self.query_quadrants()

    def query_quadrants(self):
        '''
        query_quadrants() -> NoneType

        Peers into the four coordinates around the current position.
        '''
        row, col = self.curr_pos
        self.update_seen(row + 1, col)
        self.update_seen(row - 1, col)
        self.update_seen(row, col + 1)
        self.update_seen(row, col - 1)

    def update_seen(self, row, col):
        '''
        update_seen(int, int) -> NoneType

        Checks the position and updates seen if position is empty.
        '''
        value = self.maze.get_point(row, col)

        if value == ' ' or value == "E":
            self.seen.add((row, col))

        if value == 'E':
            self.end = (row, col)

    def perform_search(self):
        '''
        perform_search() -> NoneType

        Continues to move around until all all nodes have been visited.
        '''
        while True:
            unvisited = self.seen.difference(self.visited)
            # print(self.seen, self.visited, unvisited)
            if len(unvisited) == 0:
                break

            row, col = self.curr_pos

            # choose a direction to go
            if (row + 1, col) in unvisited:
                self._update_pos(row + 1, col)
            elif (row - 1, col) in unvisited:
                self._update_pos(row - 1, col)
            elif (row, col + 1) in unvisited:
                self._update_pos(row, col + 1)
            elif (row, col - 1) in unvisited:
                self._update_pos(row, col - 1)
            else:
                self._update_pos()

            self.query_quadrants()
            time.sleep(.1)
            os.system("clear")
            print(self)
            if self.end is not None:
                break

    def _update_pos(self, row=None, col=None):
        '''
        update_pos(int, int) -> NoneType

        Updates current position.
        '''

        if row is None or col is None:
            self.curr_pos = self.path.pop()
            return

        self.curr_pos = (row, col)
        self.path.append(self.curr_pos)
        self.visited.add(self.curr_pos)

    def __str__(self):
        '''
        __str__() -> str

        Print the current state of the maze.
        '''
        return self.maze.__str__(self.visited, self.curr_pos)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid usage:")
        print("\nmaze_solver.py MAZE")
        sys.exit(0)

    maze = Maze(sys.argv[1])
    if maze is None:
        print("Unable to load maze: {}".format(sys.argv[1]))
        sys.exit(0)

    solver = Solver(maze)
    solver.perform_search()
