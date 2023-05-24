from collections import defaultdict
    
n, m = map(int, input().split())

participants = []
colors = defaultdict(int)
for _ in range(n):
    participants.append(input())

color = 1
for _ in range(m):
    
    src, dest = input().split()
    if not (colors[src] or colors[dest]):
        colors[src] = color
        colors[dest] = color
        color += 1
    else:
        colors[src] = color[src] or colors[dest]
        colors[dest] = colors[src]

visited = set ()
count = 0

answer = []
for participant in participants:
    if colors[participant] and colors[participant] not in visited:
        visited.add(colors[participant])
        answer.append(participant)
        count += 1
    elif not colors[participant]:
        answer.append(participant)
        count += 1
    

print(count)
answer.sort()

for participant in answer:
    print(participant)



    
