#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(2*10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def inOrderTraversal(tree, result, root):
  if root != -1:
    inOrderTraversal(tree, result, tree[root][1])
    result.append(tree[root][0])
    inOrderTraversal(tree, result, tree[root][2])

def IsBinarySearchTree(tree):
  result = []
  inOrderTraversal(tree, result, 0)
  return all(map(lambda i, j: i <= j, result[:-1], result[1:]))


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
