# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(input().split(" "))
n = int(input())

otherSets = []
ans = True

for _ in range(n):
    otherSets.append(set(input().split()))

for subset in otherSets:
    ans = ans and subset.issubset(setA)
print(ans)