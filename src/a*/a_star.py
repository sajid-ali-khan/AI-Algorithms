import time
from collections import defaultdict
from heapq import heappush, heappop

def read_graph(file_name) -> dict:
    graph = defaultdict(list)
    with open(file_name, 'r') as file:
        for line in file:
            a, b, c = line.split()
            c = int(c)
            graph[a].append((b, c))
            graph[b].append((a, c))
    return graph

def read_heuristics(file_name) -> dict:
    heuristics = {}
    with open(file_name, 'r') as file:
        for line in file:
            v, h = line.split()
            heuristics[v] = int(h)
    return heuristics

def a_star(start, goal, graph, heuristics) -> (list, int):
    open_list = [(heuristics[start], 0, start)]  # (estimated total cost, path cost, current city)
    visited = {}  # Track the best cost to reach each node
    closed_list = set()  # Keep track of fully explored nodes
    parent_map = {start: None}  # To reconstruct the path

    while open_list:
        estimated_cost, path_cost, city = heappop(open_list)

        if city in closed_list:
            continue
        closed_list.add(city)

        if city == goal:
            path = []
            while city is not None:
                path.append(city)
                city = parent_map[city]
            return path[::-1], path_cost  # Return reversed path

        for dest, cost in graph[city]:
            new_cost = path_cost + cost
            if dest not in closed_list and (dest not in visited or new_cost < visited[dest]):
                visited[dest] = new_cost
                priority = new_cost + heuristics[dest]
                heappush(open_list, (priority, new_cost, dest))
                parent_map[dest] = city  # Track the path

    return []

def main() -> None:
    graph = read_graph('graph-for-a*.txt')
    heuristics = read_heuristics('heuristics.txt')

    start = input("Enter the start city : ")[0].lower()
    time.sleep(0.4)
    print("The goal city is BUCHAREST(b).\n")
    time.sleep(0.4)
    hops, path_cost = a_star(start, 'b', graph, heuristics)
    if hops:
        print('Found path:', ' -> '.join(hops))
        print(f'Path cost = {path_cost}')
    else:
        print('No path found.')

if __name__ == '__main__':
    main()
