n = int(input())
if n == 0:
    print(0)
else:
    arr = [0]*n
    arr[0] = 1

    if n > 1:
        arr[1] = 1
        for i in range(2,n):
            arr[i] = arr[i-1] + arr[i-2]

    print(arr[n-1])
