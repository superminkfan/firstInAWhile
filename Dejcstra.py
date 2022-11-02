from collections import defaultdict, deque
import sys


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination]


# , list(full_path)

if __name__ == '__main__':
    graph = Graph()

    firstLine = sys.stdin.readline()
    nodes, edges = firstLine.split(' ')
    # print(nodes + " " + edges)
    # print("hui")

    for node in range(1, int(nodes) + 1):
        # print(node)
        graph.add_node(node)

    for i in range(int(edges)):
        v1, v2, w = sys.stdin.readline().split(" ")
        # print(v1 + " " + v2 + " " + w)
        graph.add_edge(int(v1), int(v2), int(w))

    firstLine = sys.stdin.readline()
    start, finish = firstLine.split(' ')
    # print(start + " " + finish)

    try:
        print(shortest_path(graph, int(start), int(finish)))
    except Exception:
        print(-1)

