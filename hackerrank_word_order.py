# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())

words = []

for i in range(n):
    words.append(input())
res = dict(Counter(words))
print(len(res))
for word in res:
    print(res[word], end = ' ')

