#Uses python3
import sys
import math

def distance(v1,v2,x,y):
    return math.sqrt((x[v1]-x[v2])**2 +  (y[v1]-y[v2])**2)

def minimum_distance(x, y):

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
            MST.append(edge)
            result += edge[2]
            disjoint_struct = list(map(lambda  x: disjoint_struct[edge[0]] if x == disjoint_struct[edge[1]] else x, disjoint_struct))

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
