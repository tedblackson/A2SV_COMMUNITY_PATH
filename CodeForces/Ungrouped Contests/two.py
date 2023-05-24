
def quickSort(arr, left, right):
    if right - left <= 1:
        return
    write = left + 1
    pivot = arr[left]
    for read in range(left + 1, right + 1):
       if arr[read] <= pivot:
           arr[read], arr[write] = arr[write], arr[read] 
           write += 1
    arr[write - 1] , arr[left] = arr[left], arr[write - 1]
    quickSort(arr, left , write - 2)
    quickSort(arr, write, right)
 
arr = [4,3,5,6,6,32,-9]
 
quickSort(arr, 0, len(arr) - 1)

print(arr)