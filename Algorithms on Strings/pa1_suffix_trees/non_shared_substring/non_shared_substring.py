# python3
import sys, threading
from collections import deque

sys.setrecursionlimit(2*10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node(object):
  def __init__(self, lab):
      self.lab = lab # lab on path leading to this node
      self.out = {}  # outgoing edges; maps characters to nodes
      self.type = 'L'
      self.visited = False
      self.parent = None

def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labs of its edges (the corresponding
  substrings of the text) in any order.
  """
  root = Node(None)
  root.out[text[0]] = Node(text)

  for i in range(1, len(text)):
    cur = root
    j = i
    while j < len(text):
      if text[j] in cur.out:
        child = cur.out[text[j]]
        lab = child.lab

        k = j + 1
        while k - j < len(lab) and text[k] == lab[k - j]:
          k += 1

        if k - j == len(lab):
          cur = child
          j = k
        else:
          cExist, cNew = lab[k-j], text[k]
          mid = Node(lab[:k-j])
          mid.out[cNew] = Node(text[k:])
          child.lab = lab[k-j:]
          mid.out[cExist] = child
          cur.out[text[j]] = mid
      else:
         cur.out[text[j]] = Node(text[j:])
  return root

def explore(root, Lleaves):
    root.visited = True
    if len(root.out) == 0:
        if '#' not in root.lab:
            root.type = 'R'
        else:
            Lleaves.append(root)
    else:
        for _, node in root.out.items():
            if not node.visited:
                node.parent = root
                explore(node, Lleaves)
        for _, node in root.out.items():
            if node.type == 'R':
                root.type = 'R'

def shortest_uncommon_string(root):
    Lleaves = []
    explore(root, Lleaves)
    results = []

    for leaf in Lleaves:
        char = ''
        substring = ''
        cur = leaf.parent

        if leaf.lab[0] == '#' and cur.type == 'R':
            continue
        elif cur.type == 'R':
            char += leaf.lab[0]

        while cur != root:
            substring = cur.lab + substring
            cur = cur.parent

        substring += char
        results.append(substring)

    result = min(results, key=lambda x:len(x))
    return result

def solve (p, q):
    text = p + '#' + q + '$'
    root = build_suffix_tree(text)
    return shortest_uncommon_string(root)

if __name__ == '__main__':
    p = sys.stdin.readline ().strip ()
    q = sys.stdin.readline ().strip ()

    ans = solve (p, q)

    sys.stdout.write (ans + '\n')
