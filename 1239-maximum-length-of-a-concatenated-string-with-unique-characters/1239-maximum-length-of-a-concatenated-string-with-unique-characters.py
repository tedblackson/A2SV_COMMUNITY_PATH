class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        n = len(arr)
        
        def backtrack(temp, cur):
            nonlocal ans
            
            for i in range(cur, n):
                temp.append(arr[i])
                word = ''.join(temp)
                unique = len(set(word))
                if unique != len(word):
                    temp.pop()
                    continue
                ans = max (ans, unique)
                backtrack(temp , i + 1)
                temp.pop()
        backtrack([], 0)
        return ans
    
                
        
        
                    
        
            
        
        