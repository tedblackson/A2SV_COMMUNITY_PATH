size = list(map(int, input().split()))

first = list(map(int, input().split()))
second = list(map(int, input().split()))



answer = []
one = two = 0

while one < size[0] and two < size[1]:  
    
    if first[one] <= second[two]:
        answer.append(first[one])
        one += 1
    else:
        answer.append(second[two])
        two +=1

answer.extend(first[one:])
answer.extend(second[two:])

print(*answer)
