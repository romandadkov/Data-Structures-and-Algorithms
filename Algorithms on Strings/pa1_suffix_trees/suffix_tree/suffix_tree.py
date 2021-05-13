# python3
import sys

from collections import deque

class Node(object):
  def __init__(self, lab):
      self.lab = lab # label on path leading to this node
      self.out = {}  # outgoing edges; maps characters to nodes

def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding
  substrings of the text) in any order.
  """
  result = []
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
          # we fell off in middle of edge
          cExist, cNew = lab[k-j], text[k]
          # create “mid”: new node bisecting edge
          mid = Node(lab[:k-j])
          mid.out[cNew] = Node(text[k:])
          # original child becomes mid’s child
          child.lab = lab[k-j:]
          mid.out[cExist] = child
          # original child’s label is curtailed
          # print('j-', j, 'label', child.lab)
          # mid becomes new child of original parent
          cur.out[text[j]] = mid
      else:
        # Fell off tree at a node: make new edge hanging off it
         cur.out[text[j]] = Node(text[j:])

  queue = deque()
  queue.append(root)
  while queue:
      u = queue.popleft()
      if u != root:
          result.append(u.lab)
      for _, node in u.out.items():
          queue.append(node)

  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))