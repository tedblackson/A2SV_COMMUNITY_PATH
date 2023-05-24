def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)
    return merge(left_half, right_half)

def merge(left, right):
    one = two = 0
    ans = []
    while one < len(left) and two < len(right):
        
        if left[one] <= right[two]:
            ans.append(left[one])
            one += 1
        else:
            ans.append(right[two])
            two += 1
    ans.extend(left[one:])
    ans.extend(right[two:])
    return ans
            
            

def test():
    assert mergeSort(0, 5, [3, 0, 2, -5, 10, 2]) == [-5, 0, 2, 2, 3, 10], "Not Implemented Properly"
    assert mergeSort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not Implemented Properly"
    assert mergeSort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not Implemented Properly"
    print("Great Job !!!")
    
test()