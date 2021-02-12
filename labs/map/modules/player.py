#!/usr/bin/env python3
'''
A Player class.
'''


class Player:
    '''
    Player class
    '''
    def __init__(self, name, curr_position=None):
        self.name = name
        self.curr_position = curr_position
        self.visited = set()
        self.visited.add(self.curr_position)

    def __str__(self):
        '''
        Return a string of player statistics.
        '''
        visited = len(self.visited)

        return f'Name: {self.name}\nLocations Visited: {visited}'

    def move(self, name):
        '''
        Attempt to move the player.
        '''
        prev_position = self.curr_position

        for edge in self.curr_position.edges:
            if name.lower() == edge.name.lower():
                self.curr_position = edge
                self.visited.add(edge)

        # check to see if a valid state name was found
        if prev_position == self.curr_position:
            raise ValueError

