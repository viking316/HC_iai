from collections import deque

def bfs(grid, start, food, rows, cols):
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # UP, LEFT, RIGHT, DOWN
    direction_names = ["UP", "LEFT", "RIGHT", "DOWN"]
    
    queue = deque([start])
    visited = set()
    visited.add(start)
    parents = {}
    explored_nodes = []

    while queue:
        current = queue.popleft()
        explored_nodes.append(current)

        if current == food:
            break

        r, c = current
        for i, (dr, dc) in enumerate(directions):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != '%':
                queue.append((nr, nc))
                visited.add((nr, nc))
                parents[(nr, nc)] = current

    return explored_nodes, parents

def reconstruct_path(parents, start, goal):
    path = []
    step = goal
    while step != start:
        path.append(step)
        step = parents[step]
    path.append(start)
    path.reverse()
    return path

# Input handling
pacman_start = tuple(map(int, input().split()))
food_position = tuple(map(int, input().split()))
rows, cols = map(int, input().split())

grid = []
for _ in range(rows):
    grid.append(input().strip())

explored_nodes, parents = bfs(grid, pacman_start, food_position, rows, cols)

# Output the number of explored nodes
print(len(explored_nodes))
for node in explored_nodes:
    print(f"{node[0]} {node[1]}")

# Output the distance and the final path from the start to the food
if food_position in parents or pacman_start == food_position:
    path = reconstruct_path(parents, pacman_start, food_position)
    distance = len(path) - 1
    print(distance)
    for node in path:
        print(f"{node[0]} {node[1]}")
else:
    print(0)
    print(f"{pacman_start[0]} {pacman_start[1]}")

"""
 sample input:

3 9
5 1
7 20
%%%%%%%%%%%%%%%%%%%%
%--------------%---%
%-%%-%%-%%-%%-%%-%-%
%--------P-------%-%
%%%%%%%%%%%%%%%%%%-%
%.-----------------%
%%%%%%%%%%%%%%%%%%%%
"""
