# python3
import queue

class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def network(self, n, m, adj_matrix):
        graph = [[0] * (n + m + 2) for _ in range(n + m + 2)]
        for i in range(1, n + 1):
            graph[0][i] = 1
            for j in range(m):
                graph[i][n + 1 + j] = adj_matrix[i - 1][j]
        for k in range(n + 1, n + m + 1):
            graph[k][-1] = 1
        return graph

    def reachable(self, graph, path):
        t = len(graph)
        visited = [False] * t
        queue = [0]
        visited[0] = True
        while queue:
            cur = queue.pop(0)
            if cur == t - 1:
                return True
            for vertex in range(t):
                if not visited[vertex] and graph[cur][vertex] > 0:
                    queue.append(vertex)
                    visited[vertex] = True
                    path[vertex] = cur
        return visited[t - 1]

    def find_matching(self, adj_matrix):
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        graph = self.network(n, m, adj_matrix)
        k = len(graph)
        path = list(range(k))
        while self.reachable(graph, path):
            min_flow = float('inf')
            v = k - 1
            while v != 0:
                u = path[v]
                min_flow = min(min_flow, graph[u][v])
                v = u
            v = k - 1
            while v != 0:
                u = path[v]
                graph[u][v] -= min_flow
                graph[v][u] += min_flow
                v = u

        matches = [-1] * n
        for i in range(k):
            if graph[k-1][i] == 1:
                person = i - n - 1
                flight = graph[i].index(1)
                matches[flight - 1] = person
        return matches

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
