![SCOA](https://github.com/stem-club-of-america/SCOA/blob/main/images/SCOA_Logo_Small.png)

# Map
In this lab, we'll work with classes, graphs, and JSON (JavaScript Object Notation).  Essentially, the JSON file has a list of states and their adjacent states.  We'll use this information to build of graph of nodes (states) and their edges to other nodes (states).  We won't do anything complicated with that resulting graph other than to print out the adjacent states to where our player is currently located.

## Difficulty
4 / 5

## Project layout

A tree of the finished lab directory:
```tree
.
├── game_files
│   └── locations.json
├── modules
│   ├── __init__.py
│   ├── location.py
│   ├── player.py
│   └── __pycache__
│       ├── __init__.cpython-38.pyc
│       ├── location.cpython-38.pyc
│       └── player.cpython-38.pyc
├── README.md
└── states.py
```

### Files
* states.py -> the main program
* locations.json ->  a data file that will form the basis of our graph
* __init__.py -> help with importing our location and player library files
* location.py -> specifies a Location class
* player.py -> specifies a player class

## Graphs
Graphs can be applied to all sorts of problems.  The main components are:
* Node -> the things being connected
* Edge -> the connectors
* Cost -> an optional cost involved in traversing the edge or visiting the node

The current JSON file contains states East of the Mississippi River:

```json
{
   "1": {
		"name": "Maine",
		"capital": "Augusta",
		"edges": ["2"]
	},
	"2": {
		"name": "New Hampshire",
		"capital": "Concord",
		"edges": ["1", "3", "4"]
	},
```

We can see a state (the node) and its edges. We can read in this file easily:

```python3
import json

with open(filename, 'r') as f:
	l_defs = json.load(f)
```

Now we have a dictionary where the key is a location id and the value of the dictionary is another dictionary of the locations attributes.  We can create a class to store this information and then iterate across this dictionary to create location objects:

```python3
class Location:
    '''
    Location class
    '''
    def __init__(self, location_id, name, capital, start=False):
        self.location_id = location_id
        self.name = name
        self.capital = capital
        self.start = start
        self.edges = set()a
	
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
```

```python3
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
```

Now the locations are linked to their adjacent locations.  All we have to do now is assign a starting location to a player.

## Player
Lets create a player class that can move around our graph.

```python3
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
```


## Game Loop
Now we just need to create a loop for the game to run:
```python3
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
```

## BONUS
For advanced students you may consider
1. Adding additional states to the graph
1. Use Dijkstra's Shortest Path algorithm to discover the shortest pathway between any two states using hop count as the metric.

