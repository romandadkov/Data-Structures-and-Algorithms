#Uses python3

import sys

sys.setrecursionlimit(200000)

def dfs_explore(adj, used, order, x):
    used[x] = True
    for vertex in adj[x]:
        if not used[vertex]:
            dfs_explore(adj, used, order, vertex)
    order.append(x)

def dfs(adj):
    used = [False] * len(adj)
    order = []
    for i in range(len(adj)):
        if not used[i]:
            dfs_explore(adj, used, order, i)
    order.reverse()
    return order

def explore(adj, visited, x):
    visited[x] = True
    for vertex in adj[x]:
        if not visited[vertex]:
            explore(adj, visited, vertex)

def number_of_strongly_connected_components(adj, reverse_adj):
    result = 0
    vertexes = dfs(reverse_adj)
    visited = [False] * len(reverse_adj)
    for vertex in vertexes:
        if not visited[vertex]:
            explore(adj, visited, vertex)
            result += 1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    reverse_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        reverse_adj[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj, reverse_adj))

# 4,4

# 1,2,
# 4,1,
# 2,3,
# 3,1


# 5,7

# 2,1,
# 3,2,
# 3,1,
# 4,3,
# 4,1,
# 5,2,
# 5,3