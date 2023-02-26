N , S = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
total = 0
maximum = 0

for end in range(len(arr)):
    total += arr[end]
    while total > S:
        total -= arr[start]
        start += 1
    maximum = max(maximum, end - start + 1  )
    
print(maximum)
    
    