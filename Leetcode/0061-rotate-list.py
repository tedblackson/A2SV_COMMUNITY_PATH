# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        if k == count or k % count == 0:
            return head
        
        
        cur = head
        for _ in range(count - k % count - 1):
            cur = cur.next
        rotated = cur.next
        cur.next = None
        cur = rotated
        
        for _ in range(k % count - 1):
            cur = cur.next
        cur.next = head
        
        return rotated
        
