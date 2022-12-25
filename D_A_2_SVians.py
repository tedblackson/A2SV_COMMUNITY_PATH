from collections import Counter
n = int(input())

members = input().split()
bad = set(input().split())

count = 0

nameCount = {}
excellent = []

for member in members:
    nameCount[member] = Counter(member)


for member , counted in nameCount.items():
    
    temp = list(counted.values())[0]

    state = True
    
    for count in counted.values():
        state = state and (count == temp)
    if state and member not in bad :
        excellent.append(member)
        
print(len(excellent))
    
    
    
    


        