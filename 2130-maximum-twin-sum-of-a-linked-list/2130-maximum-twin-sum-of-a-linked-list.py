# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        def reverse(node):
            prev = None
            while node:
                nextt = node.next
                node.next = prev
                prev = node
                node = nextt
                
            return prev
        
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        slow = reverse(slow)
        maximum = 0
        cur = head
        
               
        
        while slow:
            curSum = slow.val + cur.val
            
            maximum = max(curSum , maximum)
            slow = slow.next
            cur = cur.next
        return maximum
        
        