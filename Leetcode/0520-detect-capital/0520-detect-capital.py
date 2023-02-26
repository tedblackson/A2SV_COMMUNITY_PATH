class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if word[0].isupper():
            if len(word) > 1 and word[1].islower():
                return word[1:].islower()
            else:
                return word.isupper()
        
        if word[0].islower():
            return word.islower()
                
        
    
        
            
            
            
        