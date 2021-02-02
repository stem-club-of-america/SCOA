#!/usr/bin/env python3
import sys
from random import choices, choice


def get_types(filename):
    """
    get_types(str) -> dict

    This function reads in the various types for pokemon and records their
    weaknesses, resistances, and immunities.
    """
    types = {}

    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    for entry in lines:
        if "InternalName" in entry:
            p_type = entry.split("=")[-1].strip()
            types[p_type] = dict()
        elif "Weaknesses" in entry:
            types[p_type]["Weaknesses"] = [x.strip() for x in entry.split("=")[-1].split(",")]
        elif "Resistances" in entry:
            types[p_type]["Resistances"] = [x.strip() for x in entry.split("=")[-1].split(",")]
        elif "Immunities" in entry:
            types[p_type]["Immunities"] = [x.strip() for x in entry.split("=")[-1].split(",")]

    return types


def get_pokemon(filename, types):
    """
    get_pokemon(str, dict) -> dict

    This function reads in the names of various pokemon and records their
    type, weaknesses, resistances, and immunities.
    """
    pokemon = dict()

    with open(filename, 'r') as f:
        while line := f.readline():
            if "InternalName" in line:
                name = line.split("=")[-1].strip()
                pokemon[name] = dict()
            elif "Type1" in line:
                type_name = line.split("=")[-1].strip()
                pokemon[name]['type'] = type_name
                pokemon[name]['Weaknesses'] =  types[type_name].get('Weaknesses', [])
                pokemon[name]['Resistances'] =  types[type_name].get('Resistances', [])
                pokemon[name]['Immunities'] =  types[type_name].get('Immunities', [])

    return pokemon

def main():
    # read from the data files and build our tyeps and pokemon dictionary
    types = get_types("./files/types.txt")
    pokemon = get_pokemon("./files/pokemon.txt", types)

    # Choose our hand of pokemon as well as opponent
    hand = choices(list(pokemon), k=3)
    opponent = choice(list(pokemon))

    print("Your hand consists of: {}".format(', '.join(hand)))
    print(f"Your opponent is: {opponent}")

    # Is our opponent immune to all of our pokemon?
    no_immunities = [name for name in hand if pokemon[name]['type'] not in pokemon[opponent]['Immunities']]
    if len(no_immunities) == 0:
        print("Your apponent is immune to all of your pokemon!  Run and hide!!")
        return 0

    # Does our apponent have a weaknesses?  Lets target those first
    weaknesses = [name for name in no_immunities if pokemon[name]['type'] in pokemon[opponent]['Weaknesses']]
    if len(weaknesses) > 0:
        my_card = choice(weaknesses)
        print(f"Based on {opponent}'s weaknesses, I choose you {my_card}!")
        return 0

    # remove resistances
    no_resistances = [name for name in no_immunities if pokemon[name]['type'] not in pokemon[opponent]['Resistances']]
    if len(no_resistances) > 0:
        # opponent is neigher immune or resistant to our remaining pokemon
        my_card = choice(no_resistances)
        print(f"Based on {opponent}'s immunities and resistances, I choose you {my_card}!")
    else:
        my_card = choice(no_immunities)
        print(f"Your opponent {opponent} has some resistance to all of your remaining cards.  I choose you {my_card}!")

    return 0

if __name__ == "__main__":
    sys.exit(main())
