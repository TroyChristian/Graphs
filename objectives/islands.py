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
    row, col = node
    stepNorth = stepSouth = stepWest = stepEast = False
    if row > 0:
        stepNorth = row - 1
    if row < len(matrix) - 1:
        stepSouth = row + 1
    if col < len(matrix[row]) - 1:
        stepEast = col + 1
    if col > 0:
        stepWest = col - 1 
    
    if stepNorth is not False and matrix[stepNorth][col] == 1:
        neighbors.append((stepNorth, col))
    if stepSouth is not False and matrix[stepSouth][col] == 1:
        neighbors.append((stepSouth, col))
    if stepEast is not False and matrix[row][stepEast] == 1:
        neighbors.append((row, stepEast))
    if stepWest is not False and matrix[row][stepWest] == 1:
        neighbors.append((row, stepWest))
    

    

def dft_recursive(node):
    if node not in visted:
        ### add to visited
        visited.add(node)


        ###get neighbors
        neighbors = get_neighbors(node, matrix)


        ### for each neighbor
        for neighbor in neighbors:


        ### recurse
            dft_recursive(neighbor, visited, matrix)


def islands_counter(isles):
    visited = set()
    number_islands = 0


    for row in range(len(isles)):
        for col in range(len(isles[row])):
            node = (row, col )

            if node not in visited and isles[row][col] == 1:
                number_islands += 1

                dft_recursive(node, visited, isles)
            
    return number_islands

            
