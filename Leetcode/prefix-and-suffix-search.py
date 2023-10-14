class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()

        for i, word in enumerate(words):

            for j in range(len(word)):
                key = word[j:] + "{" + word
                self.trie.addWord(key, i)

            

    def f(self, pref: str, suff: str) -> int:
        query = suff + "{" + pref
        res = self.trie.search(query)
        
        return  -1 if  res is False else res
        


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        cur = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return cur.idx

    def addWord(self, word, pos):
        
        cur = self.root
        
        for char in word:
            idx = ord(char) - ord('a')
                                                                                                                    
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
            cur.idx = pos
        
class TrieNode():
    def __init__(self):
        self.children = [None] * 27
        self.idx = -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)