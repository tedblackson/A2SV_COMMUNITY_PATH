class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        toBeFilled = []
        count = 0
        
        for rock, capa in zip(rocks, capacity):
            toBeFilled.append(capa - rock)
        toBeFilled.sort()
        
        for space in toBeFilled:
            if additionalRocks - space >= 0:
                additionalRocks -= space
                count += 1
            else:
                break
        return count
        
        