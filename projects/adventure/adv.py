from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


    


traversal_path = []
back_trace_trav_path = [] 


def rooms_left(total_rooms, explored_vertices):
    rooms_remaining = (len(total_rooms)) - (len(explored_vertices))
    print("There are {} room(s) remaining to explore".format(rooms_remaining))
    return 



def discover_exits(current_room, explored_vertices):
#1.check room graphs second array element which holds a dictionary {"n":1} for example
#2. if the vertice we reach by going "n" not in explored_vertices set. if 1 not a in explored_vertices
#3.then "n" is a direction that leads to an new room.
    exits_discovered = []
    exits = current_room.get_exits()
    for direction in exits:
        if direction in room_graph[current_room.id][1].keys() and room_graph[current_room.id][1][direction] not in explored_vertices:
            exits_discovered.append(direction)
    
    return exits_discovered

def room_graph_printout(current_room):
    print(room_graph[current_room.id][1].keys())
    print(room_graph[current_room.id][1]['n'])

def print_current_room():
    print( "Your in room: {}".format(player.current_room.id))
    return  



def walk_rooms():
    explored_vertices = set()
    explored_vertices.add(player.current_room.id) #ex 464 if current_room.id is 464, explored_vertices = {464}
    back_trace_trav_path = []

    while len(explored_vertices) < len(room_graph.keys()): #While there are unexplored rooms
        current_room = player.current_room.id #keep track of the room player is in at this point
        print(print_current_room())
        print(rooms_left(room_graph.keys(), explored_vertices))
        print(moves_taken())
        exits_discovered = discover_exits(player.current_room, explored_vertices) # Call discover exits on current room

        if len(exits_discovered) > 0: #If there are edges from this vertex.
            
            for direction in exits_discovered:
                #add all unexplored vertices connected to the current room to the set of explored vertices
                explored_vertices.add(room_graph[current_room][1][direction])
                

                traversal_path.append(direction) # store "n" in traversal_path for example, do this for all elements in exits_discovered
                if direction == "n":
                    back_trace_trav_path.append("s")
                if direction == "s":
                    back_trace_trav_path.append("n")
                if direction == "w":
                    back_trace_trav_path.append("e")
                if direction == "e":
                    back_trace_trav_path.append("w")
                
                # if we store a direction in traversal_path, store its opposite move in back_trace_trav to be able to back out.
                player.travel(direction) #Move player
                break
        
        else:
            direction = back_trace_trav_path.pop() # if not exits_discovered, dead end, back trace. 
            player.travel(direction) #back track and repeat loop
            traversal_path.append(direction) #record that move
       
def moves_taken():
    print("Your path expends {} steps".format(len(traversal_path) + 1))
   
#print(room_graph_printout(world.starting_room))

walk_rooms() 


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



#######
# UNCOMMENT TO WALK AROUND
#######
##player.current_room.print_room_description(player)
##while True:
##    cmds = input("-> ").lower().split(" ")
##    if cmds[0] in ["n", "s", "e", "w"]:
##        player.travel(cmds[0], True)
##    elif cmds[0] == "q":
##        break
##    else:
##        print("I did not understand that command.")
