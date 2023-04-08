class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        is_prime = [True for _ in range(right + 1)]
        is_prime[0] = is_prime[1] = False
        
        i = 2
        while i * i <= right:
            
            if is_prime[i]:
                
                j = i * i
                
                while j <= right:
                    is_prime[j] = False
                    j += i
            i += 1
        
        primes = [idx for idx in range(len(is_prime)) ]
        primes = list(filter(lambda x : is_prime[x], primes))
        
        minimum = math.inf
        ans = [-1, -1]
        for i in range(0, len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if left<= primes[i] <= primes[i + 1] <= right and diff <  minimum:
                ans = [primes[i], primes[i + 1]]
                minimum = diff
        return ans
                
                