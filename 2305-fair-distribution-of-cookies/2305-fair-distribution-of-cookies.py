class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse = True)
        unfair = math.inf
        bag = [0] * k
        
        def backtrack(idx):
            nonlocal unfair
            if idx >= len(cookies):
                unfair = min(unfair, max(bag))
                return 
            if max(bag) > unfair:
                return
            
            for pos in range(k):

                bag[pos] += cookies[idx]
                
                backtrack(idx + 1)
                
                bag[pos] -= cookies[idx]
                
        backtrack(0)
        return unfair