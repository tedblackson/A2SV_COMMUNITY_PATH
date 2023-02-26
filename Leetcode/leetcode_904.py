class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = right = ans = 0
        types = {}
        
        while  right < len(fruits):
            
            if(len(types) <= 2):
                types[fruits[right]] = right
                right += 1
            
            if(len(types) > 2):
                minimum = len(fruits) - 1
                for value in types.values():
                    minimum = min(minimum, value)
                
                left = minimum +1
                
                del  types[fruits[minimum]]
                
                    
            ans  = max(ans, right - left)   
                
            
        
        return ans
                
       