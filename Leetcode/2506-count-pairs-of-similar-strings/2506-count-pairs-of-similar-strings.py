class Solution:
    def similarPairs(self, words: List[str]) -> int:

        newWord = []

        for word in words:
            temp = list(word)
            temp.sort()
            # print(temp)
            newWord.append("".join(set(temp)))
      

        count = Counter(newWord)

        pairs = 0

        for _, value in count.items():
            if value > 1:
                pairs += comb(value, 2)
        
        return pairs

