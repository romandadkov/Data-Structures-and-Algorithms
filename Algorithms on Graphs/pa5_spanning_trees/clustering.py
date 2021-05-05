#Uses python3
import sys
import math


def distance(v1,v2,x,y):
    return math.sqrt((x[v1]-x[v2])**2 +  (y[v1]-y[v2])**2)

def clustering(x, y, k):

    distances = []
    for i in range(n):
        for j in range(i,n):
            if i != j:
                distances.append([i,j,distance(i,j,x,y)])

    edges = sorted(distances, key=lambda x: x[2])

    disjoint_struct = range(n)
    MST = []
    result = 0.

    for edge in edges:
        if disjoint_struct[edge[0]] != disjoint_struct[edge[1]]:
            if len(set(disjoint_struct)) == k:
                result_edge = edge
                break
            MST.append(edge)
            result += edge[2]
            disjoint_struct = list(map(lambda  x: disjoint_struct[edge[0]] if x == disjoint_struct[edge[1]] else x, disjoint_struct))

    return result_edge[2]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
