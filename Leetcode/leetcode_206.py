# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    next_node = ListNode()
    prev_node = None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        while(head):
            self.next_node = head.next
            head.next = self.prev_node
            self.prev_node = head
            head = self.next_node
            
        return self.prev_node
            
            
            
            
    
    
        
        
            
            
            