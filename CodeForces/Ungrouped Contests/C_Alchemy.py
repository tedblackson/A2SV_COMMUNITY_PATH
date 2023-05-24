N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N -1
edward = 0
alphonso = 0

if len(arr) == 1:
    edward += arr[0]
    left += 1


while left <= right:
    if edward > alphonso:
        alphonso += arr[right]
        right -= 1
    else:
        edward += arr[left]
        left += 1
    
print(left, N - left)

        
    