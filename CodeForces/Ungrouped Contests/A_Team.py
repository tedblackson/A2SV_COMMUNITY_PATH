n = int(input())

confidence = []

for _ in range(n):
    confidence.append(list(map(int, input().split())))

solution = 0

for people in confidence:
    ctr = 0
    for level in people:
        if level == 1:
            ctr += 1
    solution = solution + 1 if ctr >= 2 else solution
print(solution)