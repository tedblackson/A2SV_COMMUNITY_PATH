n, k = map(int, input().split())

arr = list(map(int, input().split()))


arr.sort()
ans = -1

if k ==0:
    ans = arr[0] - 1
else:
    ans = arr[k -1]
    
count = 0
for ele in arr:
    if ele <= ans:
        count += 1

print(ans) if count == k and ans >= 1 else print(-1)
        

    