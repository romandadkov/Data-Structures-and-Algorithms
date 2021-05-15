# python3
import sys

def BWT(text):
    M = []
    for i in range(len(text)):
        row = text[i:] + text[:i]
        M.append(row)

    M.sort()

    return ''.join([x[-1] for x in M])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))