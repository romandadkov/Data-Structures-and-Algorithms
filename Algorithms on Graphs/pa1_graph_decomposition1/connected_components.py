#Uses python3

import sys

def explore(adj, visited, x):
    visited[x] = True
    for vertex in adj[x]:
        if not visited[vertex]:
            explore(adj, visited, vertex)


def number_of_components(adj):
    visited = [False] * len(adj)
    result = 0
    for i in range(len(adj)):
        if not visited[i]:
            explore(adj, visited, i)
            result += 1

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
