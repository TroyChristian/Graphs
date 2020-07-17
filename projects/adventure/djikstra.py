from room import Room
from player import Player
from world import World


import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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
room_keys = world.rooms.keys() 

#player = Player(world.starting_room)
"""
{
  0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
  1: [(3, 6), {'s': 0, 'n': 2}],
  2: [(3, 7), {'s': 1}],
  3: [(4, 5), {'w': 0, 'e': 4}],
  4: [(5, 5), {'w': 3}],
  5: [(3, 4), {'n': 0, 's': 6}],
  6: [(3, 3), {'n': 5}],
  7: [(2, 5), {'w': 8, 'e': 0}],
  8: [(1, 5), {'e': 7}]
}


"""
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




    

    

def shortest_path(starting_room, target_room, graph = room_graph):
    explored_vertices = set() 
    traversal_path = [] 
    back_trace_trav_path = [] 
    path_by_room_id = []
    #q = Queue()
    #q.enqueue([[starting_room]])
    starting_room = world.rooms[starting_room]
    target_room = world.rooms[target_room]
    player = Player(starting_room)
    found = target_room in explored_vertices
    
       
    explored_vertices.add(player.current_room.id) 
    back_trace_trav_path = []

    while not found: 
        current_room = player.current_room.id 
        print(current_room)
        exits_discovered = discover_exits(player.current_room, explored_vertices) 
        path_by_room_id.append(player.current_room.id)

        if len(exits_discovered) > 0: 
            
            for direction in exits_discovered:
                
                explored_vertices.add(room_graph[current_room][1][direction])
                path_by_room_id.append(room_graph[current_room][1][direction])

                

                traversal_path.append(direction)
                if direction == "n":
                    back_trace_trav_path.append("s")
                if direction == "s":
                    back_trace_trav_path.append("n")
                if direction == "w":
                    back_trace_trav_path.append("e")
                if direction == "e":
                    back_trace_trav_path.append("w")
                
               
                player.travel(direction) 
                if player.current_room == target_room:
                    #room_graph[current_room][1][direction]
                    print("ROOM FOUND")
                    print("Room route:")
                    print(path_by_room_id)
                    print(traversal_path)

                    return
                break
        
        else:
            direction = back_trace_trav_path.pop()  
            player.travel(direction) 
            traversal_path.append(direction) 
    if target_room in explored_vertices:
        return traversal_path




shortest_path(0, 8)