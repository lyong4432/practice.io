import sys

input = sys.stdin.readline
n = int(input().strip())

print(n* (n-1) *(n-2) *(n-3)//24)
