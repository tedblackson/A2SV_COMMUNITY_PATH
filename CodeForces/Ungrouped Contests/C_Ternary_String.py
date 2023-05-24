import math
N = int(input())

for _ in range(N):
    word = input()
    left = right = 0
    length = math.inf
    unique = {}

    while right < len(word):
        
        if unique.get(word[right]):
            unique[word[right]] += 1
        else:
            unique[word[right]] = 1
            
        while len(unique) == 3:
            length = min(length , right - left + 1)
            unique[word[left]] -= 1
            if unique[word[left]] == 0:
                del unique[word[left]]
            left += 1
        
        right += 1
    print(length) if length != math.inf else print(0)