from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


    

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
back_trace_trav_path = [] 
def discover_exits(current_room, explored_vertices):
    exits_discovered = []
    exits = current_room.get_exits()
    for direction in exits:
        if direction in room_graph[current_room.id][1].keys() and room_graph[current_room.id][1][direction] not in explored_vertices:
            exits_discovered.append(direction)
    
    return exits_discovered

def room_graph_printout(current_room):
    print(room_graph[current_room.id][1].keys())
    print(room_graph[current_room.id][1]['n'])

print(room_graph_printout(world.starting_room))
#1.check room graphs second array element which holds a dictionary {"n":1} for example
 #2. if the vertice we reach by going "n" not in explored_vertices set. if 1 not a in explored_vertices
#3.then "n" is a direction that leads to an new room.


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")




