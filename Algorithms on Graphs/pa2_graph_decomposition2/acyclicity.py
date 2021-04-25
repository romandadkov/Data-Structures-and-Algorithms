#Uses python3

import sys

def explore(adj, visited, x, stack, is_acyclic):
    visited[x] = True
    stack.append(x)
    for vertex in adj[x]:
        if vertex in stack:
            is_acyclic = True
        if not visited[vertex]:
            is_acyclic = explore(adj, visited, vertex, stack, is_acyclic)
    stack.pop()
    return is_acyclic

def acyclic(adj):
    visited = [False] * len(adj)
    stack = []
    is_acyclic = False
    for i in range(len(adj)):
        if not visited[i]:
            is_acyclic = explore(adj, visited, i, stack, is_acyclic)

    if is_acyclic:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
