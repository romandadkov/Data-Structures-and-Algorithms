#Uses python3

import sys


def negative_cycle(adj, cost):
    dist = [-1] * len(adj)
    prev = [None] * len(adj)
    negative_nodes = []
    dist[0] = 0
    #first run Bellamford V - 1 cycles.
    #if no negative cycles then this should be the last iteration of changes
    for i in range(len(adj)):
        for j, nodes in enumerate(adj):
            for k, node in enumerate(nodes):
                calc_cost = dist[j] + cost[j][k]
                if dist[node] > calc_cost:
                    dist[node] = calc_cost
                    prev[node] = j
                    if i == n - 1:
                        negative_nodes.append(node)

    return 0 if not negative_nodes else 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
