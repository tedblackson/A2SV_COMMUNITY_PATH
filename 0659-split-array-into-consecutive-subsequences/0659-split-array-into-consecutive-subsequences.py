class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        freq = Counter(nums)
        hashm = defaultdict(int)
        
        for num in nums:
         
            if freq[num] == 0:
                continue
            
            elif hashm[num] > 0:
                freq[num] -= 1
                hashm[num] -= 1
                hashm[num + 1] += 1
            else:
            
                for val in range(num, num + 3):
                    if freq[val] > 0:
                        freq[val] -= 1
                    else:
                        return False

                hashm[num + 3] += 1 
                
        return True
            
                
            
                
                
        
        
        
        
        
                
                
            
        
        
        
        
        
                        
                
                
                    
        
    
        
        
            
            
        
        
        
                    
                    
                
        
            
                    
                
            
            
        
        
                
            
            
        
        
        
                
            