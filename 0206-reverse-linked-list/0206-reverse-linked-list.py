# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ans = None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            self.ans = head
            return head
        self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return self.ans
    

    
        
        