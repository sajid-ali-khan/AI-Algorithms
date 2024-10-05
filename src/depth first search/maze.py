def possible_moves(current_position, maze) -> list:
    possible = []
    n, m = len(maze), len(maze[0])
    x, y = current_position[0], current_position[1]
    top = (x-1, y)
    right = (x, y+1)
    down = (x+1, y)
    left = (x, y-1)
    if top[0] >= 0 and maze[top[0]][top[1]] == 0:
        possible.append(top)

    if right[1] < m and maze[right[0]][right[1]] == 0:
        possible.append(right)

    if down[0] < n and maze[down[0]][down[1]] == 0:
        possible.append(down)

    if left[1] >= 0 and maze[left[0]][left[1]] == 0:
        possible.append(left)

    return possible


def find_path(maze, start, end) -> list:
    stack = [(start, [])]  # Stack will hold tuples of (current_position, current_path)
    visited = set()

    while stack:
        current_position, path = stack.pop()

        if current_position == end:
            return path + [current_position]  # Return the full path including the end position

        if current_position not in visited:
            visited.add(current_position)
            current_path = path + [current_position]
            for neighbor in possible_moves(current_position, maze):
                if neighbor not in visited:
                    stack.append((neighbor, current_path))

    return []  # No path found


def print_maze_with_path(maze, path):
    RED = '\033[91m'  # Red text
    RESET = '\033[0m'  # Reset to default color

    # Create a copy of the maze to modify
    maze_copy = [row[:] for row in maze]

    # Mark the path in the maze
    for x, y in path:
        maze_copy[x][y] = f'{RED}*{RESET}'

    # Print the maze
    for row in maze_copy:
        print(' '.join(map(str, row)))

def main() -> None:
    maze = []
    with open("maze.txt", 'r') as file:
        n, m = map(int, file.readline().split())
        for line in file:
            maze.append( list(map(int, line.split())) )

    start = (0, 0)
    end = (n-1, m-1)
    right_path = find_path(maze, start, end)

    if right_path:
        print('One possible path: ')
        print_maze_with_path(maze, right_path)

    else:
        print('No path possible.')

if __name__ == "__main__":
    main()




