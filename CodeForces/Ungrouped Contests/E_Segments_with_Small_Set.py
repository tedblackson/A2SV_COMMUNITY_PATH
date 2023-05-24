from collections import defaultdict
N , K = map(int, input().split())

arr = list(map(int, input().split()))

unique = defaultdict(int)


start = count = 0

for end in range(N):
    
    unique[arr[end]] += 1
    while len(unique) > K:
        
        unique[arr[start]] -= 1
        if not unique[arr[start]]:
            del unique[arr[start]]
        
        start += 1
    if len(unique) <= K:
        count += end - start + 1
        
print(count)