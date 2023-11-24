class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counted = dict(Counter(changed))
        changed.sort()
        res = []
        
        for num in changed:
            if num * 2 in counted and num in counted:
                res.append(num)
                counted[num] -= 1
                counted[num * 2] -= 1
                if counted[num] == 0:
                    del counted[num]
                if counted.get(num * 2) == 0:
                    del counted[num *2]
        return [] if len(counted) else res
        
        
                
            
            