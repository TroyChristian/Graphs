"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        #self.queue = Queue() 

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        #This is the equivalent of adding a key to our dictionary in this abstraction, its values represent its connections
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        else:
            print("That vertex already exists in the graph")

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #Take v1 as a key, add v2 to its values to represent an edge being created
        #add_edge(2,1) expected output: {2{1}}
        if v1 in self.vertices and v2 in self.vertices: # make sure both vertices exist, so we can connect
            self.vertices[v1].add(v2)
           # self.vertices[v2].add(v1) # now this is bidirectional, the edge goes both ways.



    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        #  neighbors = self.vertices[vertex_id] and that's a set.
        neighbors = self.vertices[vertex_id]
        #print(neighbors)
        print(neighbors)
        """ for neighbor in  neighbors:
            self.queue.enqueue(neighbor) """

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        current_node = 0
        queue = Queue()

        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            current_node = queue.dequeue()
            if current_node not in visited:
                visited.add(current_node)
                for neighbor in self.vertices[current_node]:
                    queue.enqueue(neighbor)

       


        




    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()

        while stack.size() > 0:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                for neighbor in vertices[current_node]:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = set()

        while queue.size() > 0:
            route = queue.dequeue()
            last_vertex = route[-1]
        ### if this node is our target node
            if current_node == destination_vertex:
        #### return it!! return TRUE
                return current_path
​
        ### if not visited
            if current_node not in visited:
        #### mark as visited
                visited.add(current_node)
        #### get its neighbors
                neighbors = self.get_neighbors(current_node)
        #### for each neighbor
                for neighbor in neighbors:
                    ## copy path so we don't mutate the original path for different nodes
                    path_copy = current_path[:]
                    path_copy.append(neighbor)
​
                ##### add to our queue
                    q.enqueue(path_copy)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
       # Mark our node as visited
       #Check if starting Vertex is our target node, if it is return it
       # iterate over starting nodes neighbors
       # check if they have been visited
       # if not visited dfs_recursive(on_that_node)
       # if this recursion returns a path, return
        ## mark our node as visited
        visited.add(vertex)
​
        ## check if it's our target node, if so return
        if vertex == destination_vertex:
            return path
​
        if len(path) == 0:
            path.append(vertex)
        
        ## iterate over neighbors
        neighbors = self.get_neighbors(vertex)
        ### check if visited
        for neighbor in neighbors:
            if neighbor not in visited: 
        #### if not, recurse with a path
                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor], visited)
        ##### if this recursion returns a path,
                if result is not None:
            ###### return from here
                    return result
​


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
