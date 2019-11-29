import os


class Node:
    '''
    A node is a point on the map that has edges to other nodes.
    '''
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.edges = []

    def add_edge(self, end_node, distance):
        '''
        add_edge(Node, int) -> None

        Adds an edge to another node.
        '''
        new_edge = Edge(self, end_node, distance)
        self.edges.append(new_edge)


class Edge:
    '''
    An edge is a connector between two nodes.
    '''
    def __init(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Maze:
    '''
    Maze loads and allows the querying of the maze.
    '''
    def __new__(cls, maze_path):
        if not os.path.exists(maze_path):
            return None
        instance = super().__new__(cls)
        instance.maze = instance.load_maze(maze_path)
        return instance

    @classmethod
    def load_maze(cls, maze_path):
        '''
        load_maze(PATH) -> list of lists

        Loads in an ascii file for the maze and returns a list of lists for the
        maze.
        '''
        new_maze = []

        # read line by line
        with open(maze_path, 'r') as maze:
            for row in maze.readlines():
                new_maze.append([col for col in row.rstrip('\n')])

        return new_maze

    def get_point(self, row, col):
        '''
        get_point(int, int) -> str

        Returns the character at the row and column or None if not found.
        '''
        try:
            return self.maze[row][col]
        except IndexError:
            return None

    def get_start(self):
        '''
        get_start() -> tuple

        Returns a tuple of the row and column numbers that identifies where 'S'
        is in the maze.
        '''
        for row, row_list in enumerate(self.maze):
            for col, val in enumerate(row_list):
                if val == 'S':
                    return (row, col)

        return None

    def __str__(self):
        return '\n'.join((''.join(row) for row in self.maze))
