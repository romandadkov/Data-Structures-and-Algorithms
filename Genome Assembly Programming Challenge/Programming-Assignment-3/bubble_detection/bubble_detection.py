# python3
import sys
import itertools

def add_edge(graph, left, right):
    graph.setdefault(left, [set(), 0])
    graph.setdefault(right, [set(), 0])

    if right not in graph[left][0]:
        graph[left][0].add(right)
        graph[right][1] += 1

def paths_disjoint(pair):
    return len(set(pair[0]) & set(pair[1])) == 2 # only V and W are shared

def dfs(graph, paths, path, start, current, depth, threshold):
    if current != start and graph[current][1] > 1:
        paths.setdefault((start, current), list()).append(path[:])

    if depth == threshold:
        return

    for next_ in graph[current][0]:
        if next_ not in path:
            path.append(next_)
            dfs(graph, paths, path, start, next_, depth + 1, threshold)
            path.remove(next_)

if __name__ == "__main__":
    data = sys.stdin.read().split()
    k, threshold, reads = int(data[0]), int(data[1]), data[2:]

    graph = {}
    paths = {}
    bubbles = 0

    # build kmers
    break_read = lambda read: [ read[j:j + k] for j in range(len(read) - k + 1) ]
    kmers = [ kmer for read in reads for kmer in break_read(read) ]

    # build deBruijn graph
    for kmer in kmers:
        left, right = kmer[:-1], kmer[1:]
        if left != right:
            add_edge(graph, left, right)


    # bubbles counting
    for k, v in graph.items():
        if len(graph[k][0]) > 1:
            dfs(graph=graph, paths=paths, path=[k], start=k, current=k, depth=0, threshold=threshold)

    for _, candidates_list in paths.items():
        for pair in itertools.combinations(candidates_list, r=2):
            if paths_disjoint(pair):
                bubbles += 1

    print(bubbles)
