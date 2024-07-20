def dfs_pacman(grid, pacman_start, food_position, rows, cols):
    stack = []
    visited = set()
    parents = {}
    
    start = pacman_start
    stack.append(start)
    visited.add(start)
    
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # UP, LEFT, RIGHT, DOWN
    
    explored_nodes = []
    found = False
    
    while stack:
        current = stack.pop()
        explored_nodes.append(current)
        
        if current == food_position:
            found = True
            break
        
        r, c = current
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != '%':
                stack.append((nr, nc))
                visited.add((nr, nc))
                parents[(nr, nc)] = (r, c)
    
    if not found:
        return explored_nodes, [], 0
    
    # Reconstruct path from food_position to pacman_start
    path = []
    step = food_position
    while step != pacman_start:
        path.append(step)
        step = parents[step]
    path.append(pacman_start)
    path.reverse()
    
    return explored_nodes, path, len(path) - 1


# Input handling
pacman_start = tuple(map(int, input().split()))
food_position = tuple(map(int, input().split()))
rows, cols = map(int, input().split())

grid = []
for _ in range(rows):
    grid.append(input().strip())

explored_nodes, path, distance = dfs_pacman(grid, pacman_start, food_position, rows, cols)

# Output
print(len(explored_nodes))
for node in explored_nodes:
    print(f"{node[0]} {node[1]}")

print(distance)
for node in path:
    print(f"{node[0]} {node[1]}")
