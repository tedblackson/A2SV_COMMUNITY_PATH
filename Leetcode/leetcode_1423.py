class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = right =  total = ans = 0
        minimum = float('inf')
        
    
        for val in cardPoints:
            total += val
        wsum = 0
        while right < len(cardPoints):
                wsum += cardPoints[right]
                while(right - left + 1 >  len(cardPoints) - k):
                    wsum -= cardPoints[left]
                    left += 1
                   
                if(right - left + 1 == len(cardPoints) - k):
                    minimum = min(minimum , wsum)
                    ans = max(total - minimum, ans)
               
                right += 1
        
        return ans
            
        