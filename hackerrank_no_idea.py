# Enter your code here. Read input from STDIN. Print output to STDOUT
size = input().split(" ")
happiness = 0
arr = input().split(" ")
liked = set(input().split(" "))
disliked = set(input().split(" "))
for ele in arr:
    if ele in liked:
        happiness += 1
    elif ele in disliked:
        happiness -= 1

print(happiness)
        
