islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


# Iterate through the matrix
# When we see a  1, if its not been visited run a traversal
#increment our islands counter
#run a traversal 
# Mark things as visited

def get_neighbors(node, matrix):
    ## take a step north, south, east, west
    if row > 0:
        stepNorth = row - 1
    

    

def dft_recursive(node):
    if node not in visted:
        ### add to visited
        visited.add(node)


        ###get neighbors
        neighbors = get_neighbors(node)


        ### for each neighbor
        for neighbor in neighbors:


        ### recurse
        dft_recursive(neighbor, visited, matrix)


def islands_counter(isles):
    for row in range(len(isles):
        for col in range(len(isles[row])):
            node = (row, col )

            if node not in visited and isles[row][col] == 1:
                number_islands += 1

                dft_recursive(node)
            
    return number_islands

            
