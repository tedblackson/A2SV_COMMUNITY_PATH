class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        primes = set()
        
        for ele in nums:
            prod = ele
            d = 2
            
            while d * d <= prod:
                
                while not prod % d:
                    prod//=d
                    primes.add(d)
                d += 1
            if prod > 1:
                primes.add(prod)
        
                
        return len(primes)