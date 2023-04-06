class Solution:
    def countArrangement(self, n: int) -> int:
        visited = set()
        count = 0
        def isBeautiful(arr):
            
            for idx, ele in enumerate(arr):
                if ele% (idx + 1) and ((idx + 1) % ele):
                    return False
            return True
        
    
        def backtrack(arr):
            nonlocal count
            
            if not isBeautiful(arr):
                return
            if len(arr) == n :
                if isBeautiful(arr):
                    count += 1
                return
            
            for ele in range(1, n + 1):
                if ele not in visited:
                    visited.add(ele)
                    arr.append(ele)
                    backtrack(arr)
                    arr.pop()
                    visited.remove(ele)
        backtrack([])
        return count
                    
                    
        