#!/usr/bin/env python3
import sys
from maze_support import Maze

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid usage:")
        print("\nmaze_solver.py MAZE")
        sys.exit(0)

    maze = Maze(sys.argv[1])
    print(maze.maze)
    print("Start: {}".format(maze.get_start()))
