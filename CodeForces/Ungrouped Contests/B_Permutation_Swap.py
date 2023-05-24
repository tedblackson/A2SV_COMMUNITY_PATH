from collections import defaultdict
from math import gcd
N = int(input())
 
for _ in range(N):
    n = int(input())
    arr = list(map(int, input().split()))
    indices = defaultdict(list)
    common = []
    for i, ele in enumerate(arr, 1):
        indices[i] = ele
    
    
    for idx, ele in enumerate(arr, 1):
        if ele < idx <= arr[ele - 1]:
            common.append(idx - ele)
    
    _common = common[0]
    
    for i in range(1, len(common)):
        _common = gcd(_common, common[i])
    
    print(_common)