#!/usr/bin/env python3
import json
import os
from random import choice
from modules import Location, Player


def load_locations(filename):
    '''
    Given a json file of locations, load them in and link them together.
    '''
    with open(filename, 'r') as f:
        l_defs = json.load(f)

    # build location objects
    locations = {}
    for l_id in l_defs:
        locations[l_id] = Location(l_id,
                                   l_defs[l_id]['name'],
                                   l_defs[l_id]['capital'],
                                   l_defs[l_id].get('start', False))

    # link up adjacent locations
    for l_id in l_defs:
        for edge_id in l_defs[l_id]['edges']:
            locations.get(l_id).link(locations.get(edge_id))
            locations.get(edge_id).link(locations.get(l_id))

    # return the start location
    l_id = choice(list(locations.keys()))
    return locations.get(l_id)

def start_game(start_location):
    player= Player(name='Wanderer', curr_position=start_location)
    while True:
        os.system('clear')
        print(player)
        print(player.curr_position)

        try:
            location_choice = \
                input('What location would you like to visit: ').lower()
            player.move(location_choice)
        except ValueError:
            # indicates an invalid user entry
            continue
        except KeyboardInterrupt:
            break


if __name__ == '__main__':

    start_location = load_locations('./game_files/locations.json')

    start_game(start_location)
