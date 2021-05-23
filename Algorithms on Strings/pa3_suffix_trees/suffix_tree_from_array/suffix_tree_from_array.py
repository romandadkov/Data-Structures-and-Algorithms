# python3
import sys

class SuffixTree:
  class Node:
    def __init__(self, node, depth, start, end):
        self.parent = node
        self.children = {}
        self.depth = depth  # string depth
        self.start = start
        self.end = end
        self.visited = False

  def __init__(self, s, order, LCP):
    self.s = s
    self.ele = ['$', 'A', 'C', 'G', 'T']
    self.order = order
    self.LCP = LCP
    self.root = self.Node(None, 0, -1, -1)

    self.STFromSA()

  def CreateNewLeaf(self, node, suffix):
    leaf = self.Node(node, len(self.s) - suffix, suffix + node.depth, len(self.s))
    node.children[self.s[leaf.start]] = leaf
    return leaf

  def BreakEdge(self, node, mid_start, offset):
    mid_char = self.s[mid_start]
    left_char = self.s[mid_start + offset]
    mid = self.Node(node, node.depth + offset, mid_start, mid_start + offset)
    mid.children[left_char] = node.children[mid_char]
    node.children[mid_char].parent = mid
    node.children[mid_char].start += offset
    node.children[mid_char] = mid
    return mid

  def STFromSA(self):
    lcp_prev = 0
    cur = self.root
    for i in range(len(self.s)):
      suffix = self.order[i]
      while cur.depth > lcp_prev:
        cur = cur.parent
      if cur.depth == lcp_prev:
        cur = self.CreateNewLeaf(cur, suffix)
      else:
         # break edge and got 3 nodes: mid, left(exist already), right(new suffix)
         mid_start = self.order[i - 1] + cur.depth  # the start of mid-node
         offset = lcp_prev - cur.depth  # the number of characters of mid-node
         mid = self.BreakEdge(cur, mid_start, offset)
         cur = self.CreateNewLeaf(mid, suffix)
      if i < len(self.s) - 1:
        lcp_prev = self.LCP[i]

  def FillEdges(self, cur, tree):
    cur.visited = True
    if cur != self.root:
      tree[cur.parent] = (cur.start, cur.end)
    for i in range(5):
      child = cur.children.get(self.ele[i], None)
      if child is not None and not child.visited:
        self.FillEdges(child, tree)


def suffix_array_to_suffix_tree(sa, lcp, text):
    """
    Build suffix tree of the string text given its suffix array suffix_array
    and LCP array lcp_array. Return the tree as a mapping from a node ID
    to the list of all outgoing edges of the corresponding node. The edges in the
    list must be sorted in the ascending order by the first character of the edge label.
    Root must have node ID = 0, and all other node IDs must be different
    nonnegative integers. Each edge must be represented by a tuple (node, start, end), where
        * node is the node ID of the ending node of the edge
        * start is the starting position (0-based) of the substring of text corresponding to the edge label
        * end is the first position (0-based) after the end of the substring corresponding to the edge label

    For example, if text = "ACACAA$", an edge with label "$" from root to a node with ID 1
    must be represented by a tuple (1, 6, 7). This edge must be present in the list tree[0]
    (corresponding to the root node), and it should be the first edge in the list (because
    it has the smallest first character of all edges outgoing from the root).
    """
    tree = {}
    suffix_tree = SuffixTree(text, sa, lcp)
    suffix_tree.FillEdges(suffix_tree.root, tree)
    return tree


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    # Build the suffix tree and get a mapping from
    # suffix tree node ID to the list of outgoing Edges.
    tree = suffix_array_to_suffix_tree(sa, lcp, text)
    """
    Output the edges of the suffix tree in the required order.
    Note that we use here the contract that the root of the tree
    will have node ID = 0 and that each vector of outgoing edges
    will be sorted by the first character of the corresponding edge label.

    The following code avoids recursion to avoid stack overflow issues.
    It uses two stacks to convert recursive function to a while loop.
    This code is an equivalent of

        OutputEdges(tree, 0);

    for the following _recursive_ function OutputEdges:

    def OutputEdges(tree, node_id):
        edges = tree[node_id]
        for edge in edges:
            print("%d %d" % (edge[1], edge[2]))
            OutputEdges(tree, edge[0]);

    """
    stack = [(0, 0)]
    result_edges = []
    while len(stack) > 0:
      (node, edge_index) = stack[-1]
      stack.pop()
      if not node in tree:
        continue
      edges = tree[node]
      if edge_index + 1 < len(edges):
        stack.append((node, edge_index + 1))
      print("%d %d" % (edges[edge_index][1], edges[edge_index][2]))
      stack.append((edges[edge_index][0], 0))
