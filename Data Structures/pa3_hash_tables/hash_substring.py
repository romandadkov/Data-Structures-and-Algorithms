# python3

import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def poly_hash(s, prime, multiplier):
    hash_val = 0
    for c in reversed(s):
        hash_val = (hash_val * multiplier + ord(c)) % prime

    return hash_val

def precompute_hashes(text, p, prime, multiplier):
    t = len(text)
    H =  list([] for _ in range(t - p + 1))
    H[t - p] = poly_hash(text[-p:], prime, multiplier)
    y = 1
    for _ in range(p):
        y = (y * multiplier) % prime
    for i in range(len(text) - p - 1, -1, -1):
        H[i] = (multiplier * H[i + 1] + ord(text[i]) - y *  ord(text[i + p])) % prime
    return H

def get_occurrences(pattern, text):
    prime = 1000000007
    multiplier = random.randint(1, prime)
    pattern_hash = poly_hash(pattern, prime, multiplier)
    H = precompute_hashes(text, len(pattern), prime, multiplier)
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if pattern_hash == H[i]
    ]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

