#!/usr/bin/env python3
import time
import os
import sys
from maze_support import Maze


class Solver:
    """
    class Solver attempts to solve a maze. It does not perform any
    optimizations (shortest path) but instead performs a quasi depth first
    search until it finds the endpoint.
    """

    def __init__(self, maze):
        # store the maze
        self.maze = maze

        # get the start position
        self.start = maze.get_start()

        # End is not known
        self.end = None

        # current position is the start position
        self.curr_pos = self.start

        # create a visited and seen set (sets will only contain unique entries)
        # visited (solver has been here)
        # seen (solver has been near here)
        self.visited = set()
        self.seen = set()

        # create a path record of where we have been (list)
        self.path = [self.start]

        # record that we have visited and seen the start
        self.visited.add(self.start)
        self.seen.add(self.start)

        # initiall look at what surrounds current position
        self._query_quadrants()

    def _query_quadrants(self):
        """
        _query_quadrants() -> NoneType

        Peers into the four coordinates around the current position.
        """
        row, col = self.curr_pos

        # update seen up, down, left, and right
        self._update_seen(row + 1, col)
        self._update_seen(row - 1, col)
        self._update_seen(row, col + 1)
        self._update_seen(row, col - 1)

    def _update_seen(self, row, col):
        """
        _update_seen(int, int) -> NoneType

        Checks the position and updates seen if position is empty.
        """
        # query the maze for what is at row, col
        value = self.maze.get_point(row, col)

        # Only update seen if position is blank or End point
        if value == " " or value == "E":
            self.seen.add((row, col))

        # if position is End Point, record it in self.end
        if value == "E":
            self.end = (row, col)

    def search(self):
        """
        search() -> NoneType

        Continues to move around until all all nodes have been visited.
        """
        while True:

            # determine if we have visited all known positions
            unvisited = self.seen.difference(self.visited)
            if len(unvisited) == 0:
                break

            row, col = self.curr_pos

            # choose a direction to go
            if self.end is not None:
                self._update_pos(self.end)
            elif (row + 1, col) in unvisited:
                self._update_pos(row + 1, col)
            elif (row - 1, col) in unvisited:
                self._update_pos(row - 1, col)
            elif (row, col + 1) in unvisited:
                self._update_pos(row, col + 1)
            elif (row, col - 1) in unvisited:
                self._update_pos(row, col - 1)
            else:
                self._update_pos()

            # take a look at surrounding positions
            self._query_quadrants()

            # take a quick sleep so we can watch the progress of the search
            time.sleep(0.1)

            # clear the screen
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

            # print solver's progress
            print(self)

            # check to see if we've reached the end
            if self.end is not None:
                break

    def _update_pos(self, row=None, col=None):
        """
        update_pos(int, int) -> NoneType

        Updates current position.
        """
        # if no position was sent, backtrack a position
        if row is None or col is None:
            self.curr_pos = self.path.pop()
            return

        # update current position
        self.curr_pos = (row, col)

        # add new position to path (list)
        self.path.append(self.curr_pos)

        # add new positoin to visited (set)
        self.visited.add(self.curr_pos)

    def __str__(self):
        """
        __str__() -> str

        Print the current state of the maze.
        """
        return self.maze.__str__(self.visited, self.curr_pos)


if __name__ == "__main__":

    # check to see if a path to the maze was passed to the program
    if len(sys.argv) != 2:
        print("Invalid usage:")
        print("\nmaze_solver.py MAZE")
        sys.exit(0)

    # create a maze object
    maze = Maze(sys.argv[1])
    if maze is None:
        print("Unable to load maze: {}".format(sys.argv[1]))
        sys.exit(0)

    # create a solver object
    solver = Solver(maze)

    # instruct solver to search for the endpoint
    solver.search()

    # check to see if solver was able to solve the maze
    if solver.end is None:
        print("Unable to solve...")
    else:
        print("Solved!!!")
