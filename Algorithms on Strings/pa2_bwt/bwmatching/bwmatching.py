# python3
import sys


def PreprocessBWT(bwt):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position
        of this character in the sorted array of
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  symbols = ['$', 'A', 'C', 'G', 'T']
  freq = {}

  for symbol in symbols:
      freq[symbol] = bwt.count(symbol)

  starts = {'$': 0}
  for i in range(1, len(symbols)):
    starts[symbols[i]] = starts[symbols[i-1]] + freq[symbols[i-1]]

  occ_count_before = {}
  # for symbol in symbols:
  #   occ_count_before[symbol] = [0]
  #   for i in range(len(bwt)):
  #     occ_count_before[symbol].append(bwt[:i + 1].count(symbol))

  for symbol in symbols:
    occ_count_before[symbol] = [0] * (len(bwt) + 1)

  for i, letter in enumerate(bwt):
    for symbol in symbols:
      a = 1 if letter == symbol else 0
      occ_count_before[symbol][i + 1] = occ_count_before[symbol][i] + a

  return starts, occ_count_before


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  top = 0
  bottom = len(bwt) - 1
  while top <= bottom:
    if pattern:
      symbol = pattern[-1]
      pattern = pattern[:-1]
      top = starts[symbol] + occ_counts_before[symbol][top]
      bottom = starts[symbol] + occ_counts_before[symbol][bottom + 1] - 1
    else:
      return bottom - top + 1
  return 0


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
