#Uses python3

import sys
import queue

def bipartite(adj):
    dist = [-1] * len(adj)
    q = queue.Queue()
    for i in range(len(adj)):
        if dist[i] != -1:
            continue
        dist[i] = 0
        q.put(i)
        while not q.empty():
            cur = q.get(0)
            for vertex in adj[cur]:
                if dist[vertex] == -1:
                    q.put(vertex)
                    dist[vertex] = dist[cur] + 1
                else:
                    if (dist[cur] - dist[vertex]) % 2 == 0:
                        return 0
            # if q.empty():
            #     try:
            #         idx = dist.index(-1)
            #         q.put(idx)
            #         dist[idx] = 0
            #     except ValueError:
            #         pass

    return 1

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
    print(bipartite(adj))

#4,4
#
#1,2,
#4,1,
#2,3,
#3,1
#
#
#5,4
#
#5,2,
#4,2,
#3,4,
#1,4
#
#
#8, 7
#
#5, 2,
#4, 2,
#3, 4,
#1, 4,
#6, 7,
#8, 6,
#7, 8