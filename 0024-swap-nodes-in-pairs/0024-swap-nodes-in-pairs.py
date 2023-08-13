# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        
        cur = dummy
        
        if not (head and head.next): return head
        
        
        
        while cur and cur.next:
            temp = cur.next
            cur.next = cur.next.next
            if cur.next:
                temp.next = cur.next.next
                cur.next.next = temp
            else:
                cur.next  = temp
            
            cur = cur.next.next if cur.next else cur.next
            
            
        return dummy.next
        
            
            
        
        