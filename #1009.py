import sys
input = sys.stdin.readline
t = int(input().strip())
nums = [[10],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
for i in range(t):
    a,b = map(int, input().split())
    a = a%10
    b = b%len(nums[a])
    print(nums[a][b-1])
