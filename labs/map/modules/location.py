#!/usr/bin/env python3
'''
Location module for establishing a location class.
'''


class Location:
    '''
    Location class
    '''
    def __init__(self, location_id, name, capital, start=False):
        self.location_id = location_id
        self.name = name
        self.capital = capital
        self.start = start
        self.edges = set()

    def __str__(self):
        '''
        Return string representation of the location.
        '''
        description = [f'{self.name}\n\t{self.capital}\n']

        if len(self.edges) > 0:
            description.append('Adjacent locations:')
            for location in sorted(self.edges, key=lambda x: x.name):
                description.append(f'\t{location.name}')

        return '\n'.join(description)

    def __len__(self):
        '''
        Return the number of adjacent states.
        '''
        return len(self.edges)

    def link(self, other):
        '''
        Link to another location.
        '''
        self.edges.add(other)

    def unlink(self, other):
        '''
        Unlink from another location.
        '''
        try:
            self.edges.remove(other)
        except KeyError:
            pass

