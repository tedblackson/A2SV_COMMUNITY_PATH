# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())

rooms = input().split(' ')

count  = dict(Counter(rooms))
for key in count:
    
    if count[key] == 1 :
        print(key)
