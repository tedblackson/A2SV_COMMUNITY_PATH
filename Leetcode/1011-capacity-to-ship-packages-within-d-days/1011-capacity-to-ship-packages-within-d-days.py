class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        low , high = max(weights), total
        
        def count(capacity):
            i = count = 0
            while i < len(weights):
                curSum = 0

                while i < len(weights) and curSum + weights[i] <= capacity:
                    curSum += weights[i]
                    i +=1
                    
                count += 1
            return count
        
        while low <= high:
            
            mid = low + (high - low)//2
            
            if count(mid) <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low
            