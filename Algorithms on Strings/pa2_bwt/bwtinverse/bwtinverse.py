# python3
import sys

def last_to_first(text):
    symbols = ['$', 'A', 'C', 'G', 'T']
    freq = {}

    for symbol in symbols:
        freq[symbol] = text.count(symbol)

    tmp = -1
    positions = {}
    for symbol in symbols:
        tmp += freq[symbol]
        positions[symbol] = tmp

    last2first = [0] * len(text)
    for i in range(len(text) - 1, -1, -1):
        last2first[i] = positions[text[i]]
        positions[text[i]] -= 1

    return last2first

def InverseBWT(bwt):
    last2first = last_to_first(bwt)
    res = ['$']
    pos = 0
    for _ in range(len(bwt) - 1):
        res.append(bwt[pos])
        pos = last2first[pos]
    res = res[::-1]
    return ''.join(res)

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))