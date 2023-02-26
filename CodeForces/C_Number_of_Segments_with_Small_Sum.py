N , S = map(int, input().split())

arr = list(map(int, input().split()))


start = 0
total = 0
count = 0

for end in range(N):
    total += arr[end]
    
    while total > S:
        total -= arr[start]
        start +=1
        
    count += end - start + 1
print(count)
    