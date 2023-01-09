class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self.value = value
        self.k = k
        self.last = -1
        

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        self.last = len(self.stream) -1 if num != self.value else self.last
        
        
        if len(self.stream) - self.last > self.k: 
            
            return True
        else:
            return False
        
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)