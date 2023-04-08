n, m, k = map(int, input().split())

emotes = list(map(int, input().split()))

emotes.sort(reverse = True)

ans = (k * emotes[0] + emotes[1]) * m // (k + 1) 
print(ans)