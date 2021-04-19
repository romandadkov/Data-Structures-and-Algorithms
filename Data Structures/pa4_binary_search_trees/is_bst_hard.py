#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(2*10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  stack = [(float('-inf'), tree[0], float('inf'))]
  while stack:
    min_val, node, max_val = stack.pop()
    if node[0] < min_val or node[0] >= max_val:
      return False
    if node[1] != -1:
      stack.append((min_val, tree[node[1]], node[0]))
    if node[2] != -1:
      stack.append((node[0], tree[node[2]], max_val))
  return True

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for _ in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if nodes == 0 or IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
