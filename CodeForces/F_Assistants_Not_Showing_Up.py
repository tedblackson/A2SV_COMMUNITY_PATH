from itertools import accumulate
n , m = map(int, input().split())

arr = [0] * (n + 1)

for _ in range(m):
    start , end = map(int, input().split() )
    
    arr[start] += 1
    arr[end + 1] -= 1
for i in range(1,len(arr)):
    arr[i] = arr[i] + arr[i - 1]
    

ans = arr.count(0)
if ans > 1:
    print('YES')
else:
    print('NO')