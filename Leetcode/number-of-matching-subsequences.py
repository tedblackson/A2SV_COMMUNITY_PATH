class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie(s)
        
        for word in words:
            trie.addWord(word)
        
        trie.countSubsequence(trie.root, 0)

        return trie.count

    

    
class Trie:
    def __init__(self, s):
        self.root = [None for _ in range(27)]
        self.searchSpace = s
        self.count = 0
    def addWord(self, word):

        cur = self.root

        for char in word:
            idx = ord(char) - ord('a')
            if not cur[idx]:
                cur[idx] = [None] * 27
            cur = cur[idx]
        if not cur[26]:
            cur[26] = 1
        else:
            cur[26] += 1
    def countSubsequence(self, root, start):
    
        for i in range(26):
            if root[i]:
                target = chr(i + ord('a'))

                exists = self.exists(start, target)

                if exists is not False:

                    self.countSubsequence( root[i], exists + 1)

                    if root[i][26]:
                        self.count += root[i][26]
                



    def exists(self, start, target):

        for i in range(start, len(self.searchSpace)):
            if self.searchSpace[i] == target:
                return i
        return False



        

