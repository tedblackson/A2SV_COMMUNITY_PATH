class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = []
        counted = Counter(words)
        words = set(words)
        words = list(words)
        words.sort(reverse = True)
        words.sort(key = lambda word: counted[word])
        
        for _ in range(k):
            ans.append(words.pop())
        return ans
        
        
        
        
        
        