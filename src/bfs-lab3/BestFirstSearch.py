import time
from collections import defaultdict
from heapq import heappush, heappop

def read_graph(file_name) -> dict:
    graph = defaultdict(list)
    with open(file_name, 'r') as file:
        for line in file:
            a, b = line.split()
            graph[a].append(b)
            graph[b].append(a)

    return graph


def read_heuristics(file_name) -> dict:
    heuristics = {}
    with open(file_name, 'r') as file:
        for line in file:
            v, h = line.split()
            heuristics[v] = int(h)

    return heuristics


def bfs(start, goal, graph, heuristics) -> list:
    hops = [[]]
    open = [(heuristics[start], start)]  # Priority queue (min-heap)
    visited = set()
    visited.add(start)
    close = set()

    while open:
        h, city = heappop(open)

        if city in close:
            continue
        close.add(city)

        hops.append(hops[-1][:])
        hops[-1].append(city)

        if city == goal:
            print('Goal found')
            return hops[-1]

        for dest in graph[city]:
            if dest not in visited:
                visited.add(dest)
                heappush(open, (heuristics[dest], dest))

        if open and open[0][1] not in graph[city]:
            hops.pop()


    print('Goal not found')
    return hops[-1]


def main() -> None:
    graph = read_graph('graph-for-bfs.txt')
    heuristics = read_heuristics('heuristics.txt')

    start = input("Enter the start city (just the first letter is enough) : ")
    time.sleep(0.4)
    print("The goal city is BUCHAREST(b).\n")
    time.sleep(0.4)
    hops = bfs(start, 'b', graph, heuristics)
    print(' -> '.join(hops))


if __name__ == '__main__':
    main()
