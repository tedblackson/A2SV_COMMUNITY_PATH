# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        less = ListNode()
        res = less
        greater = ListNode()
        secondHead = greater
        temp = head
        
        while temp:
            if temp.val < x:
                less.next = temp
                less = less.next
            else:
                greater.next = temp
                greater = greater.next
                
            temp = temp.next
        greater.next = None
        less.next = secondHead.next
        
        return res.next