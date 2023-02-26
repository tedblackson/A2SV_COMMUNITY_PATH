class Node:
    def __init__(self, val = 0, _next= None):
        self.val = val
        self.next = _next
class MyLinkedList:

    def __init__(self):
        self.head = None
       
        

    def get(self, index: int) -> int:
        temp = self.head
        
        for i in range(index):
            temp = temp.next if temp else None
        return temp.val if temp else -1
        
        

    def addAtHead(self, val: int) -> None:
        temp = Node(val, self.head)
        self.head = temp
     
    

        
        

    def addAtTail(self, val: int) -> None:
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        if temp:
            temp.next = Node(val, None)
        else:
            self.head = Node(val, None)

        

    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.head
        
        if index == 0:
            node = Node(val, self.head)
            self.head = node
            return
            
        for i in range(index - 1):
            temp = temp.next
        
        if temp and temp.next:
            temp.next = Node(val, temp.next)
        elif temp:
            temp.next = Node(val, None)
     
        
        
        
        
        
        

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        if index == 0:
            self.head = self.head.next
            return 
        for i in range(index - 1):
            temp = temp.next
        if temp and temp.next:
            temp.next = temp.next.next
        elif temp:
            temp.next = None
     
   
            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)