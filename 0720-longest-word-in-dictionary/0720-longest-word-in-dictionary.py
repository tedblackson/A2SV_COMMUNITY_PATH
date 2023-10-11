# class Solution:
#     def longestWord(self, words: List[str]) -> str:
        
#         words_set = set(words)
        
#         words.sort( reverse = True)
#         longest = ""
#         _len = 0
#         for word in words:
            
#             for i in range(1, len(word) + 1):
#                 if word[:i] not in words_set:
#                     break
#             else:
#                 if _len <= len(word):
#                     _len = len(word)
#                     longest = word
#         return longest
                    


class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = Trie()
        
        for word in words:
            trie.addWord(word)
        
        longest = ""
        for word in words:
            cur = trie.root
            
            for char in word:
                idx = ord(char) - ord('a')
                
                if not cur.children[idx].is_end:
                    break
                cur = cur.children[idx]
            else:
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
        return longest
    
class TrieNode:
    
    def __init__(self,):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    
    def addWord(self, word):
        cur = self.root
        
        for char in word:
            idx = ord(char) - ord('a')
            
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True
    


        
    
        