import sys
from itertools import permutations
input = sys.stdin.readline
n, m = map(int, input().split())
print((n-1)+(m-1)*n)
