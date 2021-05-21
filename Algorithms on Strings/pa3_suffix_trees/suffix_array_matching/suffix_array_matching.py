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
  order = sort_chars(text)
  char_class = comp_char_class(text, order)
  L = 1
  while L < len(text):
    order = sort_doubled(text, L, order, char_class)
    char_class = update_classes(order, char_class, L)
    L = 2 * L
  return order[1:]

def pattern_matching_with_suffix_array(text, pattern, suffix_array):
    left = 0
    right = len(text)
    while left < right:
        mid = (left + right) // 2
        suffix = suffix_array[mid]
        i = 0
        while i < len(pattern) and suffix + i < len(text):
            if pattern[i] > text[suffix + i]:
                left = mid + 1
                break
            elif pattern[i] < text[suffix + i]:
                right = mid
                break
            i += 1
            if i == len(pattern):
                right = mid
            elif suffix + i == len(text):
                left = mid + 1

    start = left
    right = len(text)
    while left < right:
        mid = (left + right) // 2
        suffix = suffix_array[mid]
        i = 0
        while i < len(pattern) and suffix + i < len(text):
            if pattern[i] < text[suffix + i]:
                right = mid
                break
            i += 1
            if i == len(pattern) and i <= len(text) - suffix:
                left = mid + 1

    end = right - 1
    return start, end

def find_occurrences(text, patterns):
    occs = set()

    suffix_array = build_suffix_array(text+'$')
    for pattern in patterns:
        s, e = pattern_matching_with_suffix_array(text, pattern, suffix_array)
        if s <= e:
            for i in range(s, e + 1):
                occs.add(suffix_array[i])

    return occs

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))