N = int(input())
cards = list(map(int, input().split()))
left = 0 
right = N - 1
score1 = 0
score2 = 0
turn = 0
while left <= right:
   
    if cards[right] >= cards[left]:
        if not turn%2:
            score1 += cards[right]
        else:
            score2 += cards[right]
        right -= 1
    else:
        if not turn%2:
            score1 += cards[left]
        else:
            score2 += cards[left]
        left += 1
    turn += 1
print(score1, score2)