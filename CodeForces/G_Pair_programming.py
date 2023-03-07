n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

low = ans = start = 0
high = 2 ** n
count = high // 2

while k > 0:
    mid = low + (high - low)//2  
    ans += arr[mid - 1] * count if count <= k else arr[mid - 1]  * k
    k -= count    
    count //= 2
    low = mid + 1
                
print(ans)