n = int(input())
 
is_prime = [True for _ in range( n)]
 
 
d= 2
 
while d * d <= (n + 2):
    
    if is_prime[d - 2]:
        i = d * d
        
        while i < n + 2:
            is_prime[i - 2] = False
            i += d
    d += 1
primes = set()
 
for i , val in enumerate(is_prime):
    if val:
        primes.add(i + 2)
ans = []
for i in range(2, n + 2):
    if i in primes:
        ans.append(1)
    else:
        ans.append(2)
        
if len(set(ans)) ==1:
    print(1)
else:
    print(2)
print(*ans)