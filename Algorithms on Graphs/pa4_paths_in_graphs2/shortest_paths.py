#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    prev = [None] * len(adj)
    negative_nodes = queue.Queue()
    distance[s] = 0
    reachable[s] = 1
    for i in range(len(adj)):
        changed = False
        for j, nodes in enumerate(adj):
            for k, node in enumerate(nodes):
                if  distance[j] != 10**19 and distance[node] > distance[j] + cost[j][k]:
                    changed = True
                    distance[node] = distance[j] + cost[j][k]
                    prev[node] = j
                    reachable[node] = 1
                    if i == n - 1:
                        negative_nodes.put(node)
                        shortest[node] = 0
        if not changed:
            break

    for i in range(len(adj)):
        if distance[i] < 10**19:
            reachable[i] = 1

    visited = [False] * len(adj)
    while not negative_nodes.empty():
        u = negative_nodes.get()
        visited[u] = True
        shortest[u] = 0
        for v in adj[u]:
            if visited[v] == False:
                negative_nodes.put(v)
                visited[v] = True
                shortest[v] = 0

    distance[s] = 0


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

#4 5
#1, 2, 100,
#1, 3, 100,
#3, 4, -1 ,
#4, 3, -1 ,
#4, 2, 100,
#1
#
#
#67
#1, 2, 10,
#2, 3, 5,
#1, 3, 100,
#3, 5, 7,
#5, 4, 10,
#4, 3, -18,
#6, 1, -1
#1