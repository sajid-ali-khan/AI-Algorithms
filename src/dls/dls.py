from collections import defaultdict

graph = defaultdict(list)


def read_graph(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            s, d = line.split()
            graph[s].append(d)
            graph[d].append(s)


def dls(start, goal, depth):
    path = []
    stack = [(start, 0)]
    visited = set()

    while stack:
        curr, l = stack[-1]

        if curr not in visited:
            visited.add(curr)
            path.append(curr)

        if curr == goal:
            return path

        for d in graph[curr]:
            if d not in visited and l < depth:
                stack.append((d, l + 1))
                break
        else:
            stack.pop()
            path.pop()

    return []  # Return empty list if no path found


def main():
    read_graph('demo-input.txt')
    start, goal = input('Enter the start and goal nodes (separated by a space): ').split()
    depth = int(input('Enter the depth of search: '))

    if start not in graph or goal not in graph:
        print("Error: Invalid start or goal node.")
        return

    path = dls(start, goal, depth)

    if path:
        print('Found the Goal.')
        print(' -> '.join(path))
    else:
        print('Goal Not Found within the depth limit.')


if __name__ == '__main__':
    main()
