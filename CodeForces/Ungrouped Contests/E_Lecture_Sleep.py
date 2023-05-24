size = list(map(int, input().split()))

thereoms = list(map(int, input().split()))
sleeps = list(map(int, input().split()))

mapper = {}

total = 0
for i, thereom in enumerate(thereoms):
    if sleeps[i]:
        total += thereoms[i]


left = right = 0
ans = total

while right < len(thereoms):
    if sleeps[right] == 0:
        total += thereoms[right]
    
    if right - left + 1 > size[1]:
        if sleeps[left] == 0:
            total -= thereoms[left]
        left += 1
    
    ans = max(ans, total)
    right += 1
print(ans)
        
            


    
    