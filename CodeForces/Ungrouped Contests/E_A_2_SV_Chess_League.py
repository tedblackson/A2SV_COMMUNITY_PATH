n , k = map(int, input().split())

ans = []
players = list(map(int, input().split()))
players = [(player, idx + 1) for idx , player in enumerate(players)]


def merge(left, right):
    first = second = 0
    merged = []
    while first < len(left) and second < len(right):
        
        if left[first][0] <= right[second][0]:
            if left[first][0] >= right[second][0]  - k :
                merged.append(left[first])
            first += 1
        elif right[second][0] < left[first][0]:
            if right[second][0] >= left[first][0] - k:
                merged.append(right[second])
            second += 1
    merged.extend(left[first:])
    merged.extend(right[second:])
    
        
    return merged
        
    
def mergeSort(arr, left , right):
    if left == right:
        return [arr[left]]
    mid = left + (right - left)//2
    
    lefthalf = mergeSort(arr, left , mid)
    righthalf = mergeSort(arr, mid + 1, right)

    return merge(lefthalf, righthalf)
res = mergeSort(players, 0 , len(players) - 1)
res.sort(key= lambda ele: ele[1])
ans = [ele[1] for ele in res]


print(*ans)