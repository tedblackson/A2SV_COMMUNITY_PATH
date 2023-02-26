N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N -1
leftSum = 0
rightSum = 0
edward = 0
alphonso = 0
while left <= right:
    leftSum += arr[left]
    
    while rightSum < leftSum:
        rightSum += arr[right]
        right -= 1
        alphonso +=1
    left += 1
    edward += 1    

print(edward , alphonso)

        
    