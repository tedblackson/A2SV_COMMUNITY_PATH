class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [0] * k
        self.tail = 0
        self.head = 0
        

    def enQueue(self, value: int) -> bool:
        length = self.tail - self.head 
        if length < self.size:
            self.queue[self.tail % self.size] = value
            self.tail += 1
            return True
        return False
        

    def deQueue(self) -> bool:
        length = self.tail - self.head 
        if length > 0:
            self.head += 1
            return True
        return False
        

    def Front(self) -> int:
        length = self.tail - self.head 

        return self.queue[self.head % self.size] if length else -1
        

    def Rear(self) -> int:
        length = self.tail - self.head
        return self.queue[self.tail % self.size - 1] if length else -1

    def isEmpty(self) -> bool:
        length = self.tail - self.head
        return True if not length else False

    def isFull(self) -> bool:
        length = self.tail - self.head 
        return True if length == self.size else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()