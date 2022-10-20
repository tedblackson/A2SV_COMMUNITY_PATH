# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        right = head.next  if head else None
        
        while right:
            
            if left.val == right.val:
                left.next = right.next
                right = right.next
            else:
                left = left.next
                right = right.next
        return head
                
        