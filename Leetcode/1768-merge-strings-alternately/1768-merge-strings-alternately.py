class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        word = word1 if len(word1) >= len(word2) else word2
        newS = ''

        ctr = 0
        while ctr < len(word):
            newS = newS +word1[ctr] if ctr < len(word1) else newS
            newS = newS + word2[ctr] if ctr < len(word2) else newS
            ctr += 1
        
        return newS
        


        
