class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        prefix = [0] * (1001)
        
        for passenger , start , end in trips:
            
            prefix[start] += passenger 
            prefix[end ] -= passenger
        
        for i in range(1, len(prefix)):
            if prefix[i - 1] > capacity:
                return False

            prefix[i] += prefix[i - 1]
        return True
            
            