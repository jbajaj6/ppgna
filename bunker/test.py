import numpy as np

# Define the walls
walls = {((0, 0), (0, 3)), ((-1.5, 0), (1.5, 0)), ((-1.5, 6), (1.5, 6)), ((-1.5, 0), (-1.5, 6))}
start = (0.5, 0.5)
goal = (-0.5, 0.5)

# Determine the size of the grid
xmin = min(min(point[0] for point in wall) for wall in walls)
xmax = max(max(point[0] for point in wall) for wall in walls)
ymin = min(min(point[1] for point in wall) for wall in walls)
ymax = max(max(point[1] for point in wall) for wall in walls)
width = int(np.ceil(xmax - xmin))
height = int(np.ceil(ymax - ymin))

# Create the grid and set the values of the walls to 1
grid = np.zeros((width, height))
for wall in walls:
    x1, y1 = wall[0]
    x2, y2 = wall[1]
    x1 -= xmin
    x2 -= xmin
    y1 -= ymin
    y2 -= ymin
    if x1 == x2:
        for y in range(int(y1), int(y2) + 1):
            grid[int(x1), int(y)] = 1
    else:
        for x in range(int(x1), int(x2) + 1):
            grid[int(x), int(y1)] = 1

# Define the A* search algorithm
def astar(array, start, goal):
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, end)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))

    while oheap:

        current = heapq.heappop(oheap)[1]

        if current == end:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data[::-1]

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return False

# Call the A* search algorithm with the grid, start, and goal
path = astar(grid, (int(start[0] - xmin), int(start[1] - ymin)), (int(goal[0] - xmin), int(goal[1] - ymin)))

# Convert the path back to the original coordinates
path = [(point[0] + xmin, point[1] + ymin) for point in path]

# Print the shortest path
print(path)