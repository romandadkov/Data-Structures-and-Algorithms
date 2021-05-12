# python3

import sys

def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    index = 1

    for pattern in patterns:
        cur_node = tree[0]
        for letter in pattern:
            if letter in cur_node.keys():
                cur_node = tree[cur_node[letter]]
            else:
                cur_node[letter] = index
                tree[index] = {}
                cur_node = tree[index]
                index += 1
        cur_node['$'] = {}
    return tree

def prefix_trie_matching(text, tree, ext_idx):
    index = 0
    symbol = text[index]
    current = tree[0]
    res = -1

    while True:
        if (not current) or ('$' in current):
            return res
        elif symbol in current.keys():
            current = tree[current[symbol]]
            index += 1
            res = ext_idx
            if index < len(text):
                symbol = text[index]
            elif '$' in current:
                return res
            else:
                symbol = '@'
                res = -1
        else:
            return res if '$' in current else -1

def solve (text, n, patterns):
    tree = build_trie(patterns)
    return sorted(list(set([i for i in range(len(text)) if prefix_trie_matching(text[i:], tree, i) != -1 ])))

if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    n = int (sys.stdin.readline().strip())
    patterns = []
    for i in range (n):
        patterns += [sys.stdin.readline().strip()]

    ans = solve(text, n, patterns)

    sys.stdout.write(' '.join(map(str, ans)) + '\n')
