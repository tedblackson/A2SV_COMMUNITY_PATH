class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words_set = set(words)
        
        words.sort( reverse = True)
        longest = ""
        _len = 0
        for word in words:
            
            for i in range(1, len(word) + 1):
                if word[:i] not in words_set:
                    break
            else:
                if _len <= len(word):
                    _len = len(word)
                    longest = word
        return longest
                    
                    
                    
        