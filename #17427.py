import sys
input = sys.stdin.readline

n = int(input())
hap = 0
for i in range(1,n+1):
    
    hap += i * (n//i)
    
print(hap)
