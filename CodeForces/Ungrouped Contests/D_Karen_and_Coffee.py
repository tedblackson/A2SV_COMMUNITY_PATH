n , k , q = map(int, input().split())
from itertools import accumulate

arr = [0] * 200_002

for _ in range(n):
    start, end = map(int, input().split())
    arr[start] += 1
    arr[end + 1] -=1 

arr = list(accumulate(arr))
prefix = [0] * 200_002

for i in range(len(arr)):
    if arr[i] >= k:
        prefix[i] += 1

prefix = list(accumulate(prefix))

for _ in range(q):
    start , end = map(int, input().split())
    if start - 1 >= 0:
        print(prefix[end] - prefix[start - 1])
    else:
        print(prefix[end])
    
