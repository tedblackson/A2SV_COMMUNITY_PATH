class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left = score = 0
        right = len(tokens) - 1
        
        while left <= right:
            
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1
            elif score > 0 and right - left > 1:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                left += 1
        return score