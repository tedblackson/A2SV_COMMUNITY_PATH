class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
        

    def addWord(self, word: str) -> None:
        
        cur = self.root
        
        for char in word:
            idx = ord(char) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
            
        cur.is_end = True
        
        
        
        

    def search(self, word: str) -> bool:
        
        
        res = self.dfs(self.root, word, 0)
        
        return res
                
    def dfs(self, root, word, cur):
        if not root:
            return False
        elif  root.is_end and cur == len(word):
            return True
        elif cur >= len(word):
            return False

        
        if word[cur] == ".":
            for child in root.children:
                if self.dfs(child, word, cur + 1):
                    return True
        else:
            idx = ord(word[cur]) - ord('a')

            if self.dfs(root.children[idx] , word,  cur + 1):
                return True
            
        return False
        

        
        
class TrieNode:
    
    
    def __init__(self,):
        self.children = [None for _ in range(26)]
        self.is_end = False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)