N = int(input())

arr = list(map(int, input().split()))
temp = arr.copy()
temp.sort()
 
first = 0
last = len(arr) - 1

if temp == arr:
    print('yes')
    print(first + 1, first + 1)
    exit()
    
while first <= last:
    if arr[first] == temp[first]:
        first += 1
    if arr[last] == temp[last]:
        last -= 1
    elif arr[first] != temp[first]:
        break

rev = arr[first: last + 1]
rev.reverse()

new = arr[:first] + rev  + arr[last + 1:]
if new == temp:
    print('yes')
    print(first + 1, last + 1)
else:
    print('no')
