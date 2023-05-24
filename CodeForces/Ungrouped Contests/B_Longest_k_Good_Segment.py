from collections import Counter
n, k = map(int, input().split())

arr = list(map(int, input().split()))

count1 = Counter(arr[:k - 1])
start = 0
ans = 0
location = []
for end in range(k -1 , n):
    if count1.get(arr[end]):
        count1[arr[end]] += 1
    else:
        count1[arr[end]] = 1
        
    while len(count1) > k:
        count1[arr[start]] -= 1
        
        if count1[arr[start]] == 0:
            del count1[arr[start]]
        start += 1
    if ans < end - start + 1:
        location = [start + 1, end + 1]
        ans = end - start + 1
print(*location)
    
        
        
        

