from collections import deque
n = int(input())

queue = input().split()

q = int(input())


for _ in range(q):
    target = input()
    
    for i, ele in enumerate(queue):
        if target < ele:
            print(i)
            break
    else:
        print(len(queue))
    

