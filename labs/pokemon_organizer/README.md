![SCOA](https://github.com/stem-club-of-america/SCOA/blob/main/images/SCOA_Logo_Small.png)

**Pokémon is a product of The Pokémon Company International and we are in no way affiliated with them.**

# Pokémon Organizer
In this lab we will figure out how to parse a text file for pieces of information in order to make a decision.  This would be somewhat like what a data scientist would do except without the use of advanced algorithms and data structures.  This lab is potentially too difficult for newer students not used to doing text parsing and multiple dictionaries.  Variations could however, make this less of a hurdle.

## Difficulty
5 / 5

## Scenario
Your friend has asked you to help him strategize his Pokémon battles.  He has written down each Pokémon he is aware of in a file.  Additionally, he has written down the various Pokémon types and their known weaknesses and immunities.

## Goals
1. Read in these two files and organize them for quick lookup.
1. Choose 3 random cards as your battle hand.
1. Choose 1 random card as your opponent.
1. Determine which of your 3 cards would be a good match for your opponent based on your opponents weaknesses, resistances, and immunities.  You may not have a perfect fit but you must choose one.

### Read in the two files
I would suggest storing information in a dictionary.  I would also suggest keeping it simple and only recording information you need such as the name of Pokémon, their first type (Type1), their weaknesses, resistances, and immunities.  You just need to record enough information to make some type of decision about which Pokémon to play.

#### types.txt
*types.txt* lists the Pokémon type names, weaknesses, resistances, and immunities.  Not all types have each of these though.

Example
```
[0]
Name=Normal
InternalName=NORMAL
Weaknesses=FIGHTING
Immunities=GHOST

[1]
Name=Fighting
InternalName=FIGHTING
Weaknesses=FLYING,PSYCHIC
Resistances=ROCK,BUG,DARK

[2]
Name=Flying
InternalName=FLYING
Weaknesses=ROCK,ELECTRIC,ICE
Resistances=FIGHTING,BUG,GRASS
Immunities=GROUND
```

There are many ways to parse this information out.  One way to do this would be:
```python3
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
```

> This may seem advanced for some students as the above code relies heavily on list comprehensions and a dictionary of dictionaries.  It is completely fine to use other methodologies. 

#### pokemon.txt
*pokemon.txt* is laid out very similar to *types.txt* but lists over 600 different Pokémon.

Example:
```
[1]
Name=Bulbasaur
InternalName=BULBASAUR
Type1=GRASS
Type2=POISON
BaseStats=45,49,49,45,65,65
GenderRate=FemaleOneEighth
GrowthRate=Parabolic
BaseEXP=64
EffortPoints=0,0,0,0,1,0
Rareness=45
Happiness=70
Abilities=OVERGROW
HiddenAbility=CHLOROPHYLL
Moves=1,TACKLE,3,GROWL,7,LEECHSEED,9,VINEWHIP,13,POISONPOWDER,13,SLEEPPOWDER,15,TAKEDOWN,19,RAZORLEAF,21,SWEETSCENT,25,GROWTH,27,DOUBLEEDGE,31,WORRYSEED,33,SYNTHESIS,37,SEEDBOMB
EggMoves=AMNESIA,CHARM,CURSE,ENDURE,GIGADRAIN,GRASSWHISTLE,INGRAIN,LEAFSTORM,MAGICALLEAF,NATUREPOWER,PETALDANCE,POWERWHIP,SKULLBASH,SLUDGE
Compatibility=1,7
StepsToHatch=5355
Height=0.7
Weight=6.9
Color=Green
Habitat=Grassland
RegionalNumbers=1,231
Kind=Seed
Pokedex=Bulbasaur can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun's rays, the seed grows progressively larger.
BattlerPlayerY=0
BattlerEnemyY=25
BattlerAltitude=0
Evolutions=IVYSAUR,Level,16
```

> Not every field is needed and it is possible for a Pokémon to be listed more than once.

There are many ways to parse this information out.  One way to do this would be:
```python3
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
```

While this may be advanced for some students and requires a later version of Python (Python 3.8+ due to the walrus operator ":="), similar variations are perfectly fine.  The main points are:
1. Open the file
1. Read in a line
1. Look for keywords in the line and if found, split on the "=" sign remembering to strip the newline ("\n") off the end.
1. Store the results under the appropriate field in the dictionary.

### Choose 3 random cards for your battle hand
The random module has a function called *choices* that allows you to specify the number of choices to return from an iterable.

```python3
hand = choices(list(pokemon), k=3)
```

### Choose 1 random card for your opponent
The random module has a function called *choice* that returns a single random item from the iterable.

```python3
opponent = choice(list(pokemon))
```


### Determine which of your 3 cards would be a good match
There is no best answer here but generally looking to make sure some logic was applied such:
1. Remove types your opponent is immune to.
1. Look for types our opponent has weaknesses to.
1. Try to find a type that your opponent isn't resistant to.
1. When all else fails, try one of your cards or run in the case that you have no cards that would inflict any damage due to immunities.

This could play out something like:
```python3
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
```

## Credit
> The two Pokémon text files used in this project were taken from Ian Zewiske's Pokémon Project hosted on [github.com](https://github.com/izewiske/Pokémon)
