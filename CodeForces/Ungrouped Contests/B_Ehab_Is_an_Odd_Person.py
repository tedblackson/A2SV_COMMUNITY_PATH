n = int(input())

arr = list(map(int, input().split()))

odd = False
even = False

for ele in arr:
    if ele % 2:
        odd = True
    else:
        even = True

if odd and even:
    arr.sort()

print(*arr)