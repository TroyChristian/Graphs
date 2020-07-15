
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

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2) 

    def get_neighbors(self, vertex):
        return self.vertices[vertex]


def build_graph(ancestors):
    graph = Graph()
    for parent, child in ancestors:
       

        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)

    return graph 

def earliest_ancestor(ancestors, starting_node):
    graph = build_graph(ancestors)
    stack  = Stack()
    visited = set()

    stack.push([starting_node]) #path to starting node
    longest_path = []
    aged_one = -1

    while stack.size() > 0:
        path = stack.pop() # We just popped an entire list off the "stack"
        current_node = path[-1] # Current node is the last element in that list

        #if path is longer, orpath is equal but the id is smaller
        if (len(path) > len(longest_path)) or (len(path) == len(longest_path_) and current_node < aged_one):
            longest_path = path 
            aged_one = -1 # for if they dont have an ancestor

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_neighbors(current_node)

            for parent in parents:
                new_path = path + [parent] #take our current path list, put parent in a new list, mush them.
                stack.push[new_path] #Push this new path list onto the stack

        return longest_path[-1]



    