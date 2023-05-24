
def cyclicSort(arr):
    
    for i in range(len(arr)):
        
        while arr[i] - 1 != i:
            temp = arr[i]
            arr[i] , arr[temp - 1] = arr[arr[i]- 1], arr[i]
    

arr = [3,5,2,1,4]
cyclicSort(arr)
print(arr)