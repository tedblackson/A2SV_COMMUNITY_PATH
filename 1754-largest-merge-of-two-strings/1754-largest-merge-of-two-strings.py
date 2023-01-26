class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge  = ''
        
        one = two = 0
        
        while one < len(word1) and two < len(word2):
            
            if word1[one] > word2[two]:
                merge += word1[one]
                one += 1
            elif word1[one] == word2[two]:
                if word1[one:] >= word2[two:]:
                    merge += word1[one] 
                    one += 1
                else:
                    merge += word2[two]
                    two +=1
                
            else:
                merge += word2[two]
                two += 1
        merge += word1[one:]
        merge += word2[two:]
        return merge
    
    
                
        