# python3

import sys

class Solver:
	def __init__(self, s):
		self.s = s
		self.prime_1 = 1000000007
		self.prime_2 = 1000000009
		self.multiplier = 263
		self.H1 = self.hash_table(self.prime_1)
		self.H2 = self.hash_table(self.prime_2)

	def ask(self, a, b, l):
		a_1 = self.hash_value(self.H1, self.prime_1, a, l)
		a_2 = self.hash_value(self.H2, self.prime_2, a, l)
		b_1 = self.hash_value(self.H1, self.prime_1, b, l)
		b_2 = self.hash_value(self.H2, self.prime_2, b, l)
		return a_1  == b_1 and a_2 == b_2

	def hash_table(self, prime):
		H = list([] for _ in range(len(self.s) + 1))
		H[0] = 0
		for i in range(1, len(s) + 1):
			H[i] = (H[i - 1] * self.multiplier + ord(s[i - 1])) % prime
		return H

	def hash_value(self, table, prime, start, length):
		y = pow(self.multiplier, length, prime)
		return (table[start + length] - y * table[start]) % prime


s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
