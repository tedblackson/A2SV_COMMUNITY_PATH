from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.store = SortedList()
        
        

    def addNum(self, num: int) -> None:
        self.store.add(num)
        

    def findMedian(self) -> float:
        n = len(self.store)
        
        if n & 1:
            return self.store[n//2]
        else:
            return (self.store[n//2] + self.store[n//2 - 1])/2
        
        
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()