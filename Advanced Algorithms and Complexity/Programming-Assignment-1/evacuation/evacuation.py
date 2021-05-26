# python3

import queue

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

    def available(self):
        return self.capacity - self.flow

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph

def find_path(graph, from_, to):
    visit = queue.Queue()
    visit.put((from_, []))
    visited = set()
    while not visit.empty():
        (u, p) = visit.get()
        if u in visited:
            continue

        visited.add(u)

        edges = graph.get_ids(u)

        for id in edges:
            edge = graph.get_edge(id)
            if edge.v in visited:
                continue

            if edge.available() > 0:
                if edge.v == to:
                    p.append(id)
                    return p

                next = list(p)
                next.append(id)
                visit.put((edge.v, next))

    return None

def find_min_flow(graph, p):
    min_flow_edge = min(p, key = lambda x: graph.get_edge(x).available())
    return graph.get_edge(min_flow_edge).available()

def max_flow(graph, from_, to):
    flow = 0

    while True:
        p = find_path(graph, from_, to)
        if p is None:
            break
        min_flow = find_min_flow(graph, p)
        for e in p:
            graph.add_flow(e, min_flow)
        flow += min_flow

    return flow


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))


    graph.add_edge(1-1 ,2-1, 2)
    graph.add_edge(2-1 ,5-1, 5)
    graph.add_edge(1-1 ,3-1, 6)
    graph.add_edge(3-1 ,4-1, 2)
    graph.add_edge(4-1 ,5-1 ,1)
    graph.add_edge(3-1 ,2-1, 3)
    graph.add_edge(2-1 ,4-1 ,1)