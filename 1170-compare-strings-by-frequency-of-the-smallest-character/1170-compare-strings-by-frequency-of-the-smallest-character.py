class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        wordCount = []
        queryCount = []
        
        for query in queries:
            temp = sorted(query)
            queryCount.append(temp.count(temp[0]))
        
        for word in words:
            temp = sorted(word)
            wordCount.append(temp.count(temp[0]))
        
        wordCount.sort()
        n = len(wordCount)
        answer = []
        
        
        for count in queryCount:
            best = low = 0
            high = n - 1
            
            while low <= high:
                mid = low + (high - high)//2
                if wordCount[mid] > count:
                    best = max(best, n - mid )
                    high = mid - 1
                else:
                    low =  mid + 1
            answer.append(best)
        return answer
            
                    