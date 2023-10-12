class Solution:
    def __init__(self):
        self.root = [0] * 27
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = []
        
        for word in words:
            self.addWord(word)
        
        for word in words:
            ans.append(self.search(word))
        
        return ans
        
        
        
        
    def addWord(self, word):
        
        cur = self.root
        
        for char in word:
            idx = ord(char) - ord('a')
            
            if not cur[idx]:
                cur[idx] = [0] * 27
            cur = cur[idx]
            cur[26] += 1 
        
    
    def search(self, word):
        cur = self.root
        _sum = 0
        
        for char in word:
            idx = ord(char) - ord('a')
            cur = cur[idx]
            _sum += cur[26]
            
        return _sum
            