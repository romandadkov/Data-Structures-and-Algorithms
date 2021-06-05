# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]
K = 3

def printEquisatisfiableSatFormula():
    """ https://research.ijcaonline.org/encc/number1/encc004.pdf """

    # print("3 2")
    # print("1 2 0")
    # print("-1 -2 0")
    # print("1 -2 0")

    c, v, cnt = K * len(edges) + n, n * K, 1
    print("{0} {1}".format(c, v))

    for i in range(1, n + 1):
        print("{0} {1} {2} 0".format(cnt, cnt + 1, cnt + 2))
        cnt += 3

    for edge in edges:
        print("{0} {1} 0".format(-((edge[0] - 1) * K + 1), -((edge[1] - 1) * K + 1)))
        print("{0} {1} 0".format(-((edge[0] - 1) * K + 2), -((edge[1] - 1) * K + 2)))
        print("{0} {1} 0".format(-((edge[0] - 1) * K + 3), -((edge[1] - 1) * K + 3)))


printEquisatisfiableSatFormula()
