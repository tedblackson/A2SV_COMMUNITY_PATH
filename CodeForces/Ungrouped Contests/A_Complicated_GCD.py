a, b = map(int, input().split())

def gcd (a, b):
    
    if b == 0:
        return a
    return gcd(b, a %b)
ans = a

for i in range(a, b + 1):
    ans = gcd(i, ans)

print(ans)