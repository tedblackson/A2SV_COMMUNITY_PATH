n = int(input())
count = 0
for i in range(1, n + 1):
    num = i
    d = 2
    primes = set()
    while d * d <= num:
        
        
        while not num % d:
            
            primes.add(d)
            num//= d
        d += 1
    if num > 1:
        primes.add(num)
    
    if len(primes) == 2:
        count += 1
print(count)