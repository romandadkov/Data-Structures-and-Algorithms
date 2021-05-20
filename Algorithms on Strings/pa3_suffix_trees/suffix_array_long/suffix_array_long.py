# python3
import sys

def sort_chars(text):
  symbols = ['$', 'A', 'C', 'G', 'T']
  freq = {'$': 0, "A": 0, 'C': 0, 'G': 0, 'T': 0}
  for char in text:
        freq[char] += 1
  for i in range(1, len(symbols)):
    freq[symbols[i]] += freq[symbols[i-1]]

  order = [0] * len(text)
  for i in range(len(text) - 1, -1, -1):
      freq[text[i]] -= 1
      order[freq[text[i]]] = i

  return order


def comp_char_class(text, order):
  char_class = [0] * len(text)
  for i in range(1, len(text)):
    a = 0 if text[order[i]] == text[order[i - 1]] else 1
    char_class[order[i]] = char_class[order[i - 1]] + a
  return char_class


def sort_doubled(text, L, order, char_class):
  count = [0] * len(text)
  new_order = [0] * len(text)
  for i in range(len(text)):
    count[char_class[i]] += 1
  for i in range(1, len(text)):
    count[i] += count[i - 1]
  for i in range(len(text) - 1, -1, -1):
    start = (order[i] - L + len(text)) % len(text)
    cl = char_class[start]
    count[cl] -= 1
    new_order[count[cl]] = start
  return new_order


def update_classes(order, char_class, L):
  n = len(order)
  new_class = [0] * n
  for i in range(1, n):
    cur = order[i]
    mid = (cur + L) % n
    prev = order[i - 1]
    mid_prev = (prev + L) % n
    a = 0 if char_class[cur] == char_class[prev] and char_class[mid] == char_class[mid_prev] else 1
    new_class[cur] = new_class[prev] + a
  return new_class

def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  order = sort_chars(text)
  char_class = comp_char_class(text, order)
  L = 1
  while L < len(text):
    order = sort_doubled(text, L, order, char_class)
    char_class = update_classes(order, char_class, L)
    L = 2 * L
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))


#Input:
#AACGATAGCGGTAGA$
#
#Correct output:
#15 14 0 1 12 6 4 2 8 13 3 7 9 10 11 5
