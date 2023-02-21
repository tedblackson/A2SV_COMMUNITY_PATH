# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy
        rem = 0
        while l1 and l2:
            # print(l1.val,l2.val)
            curSum = l1.val + l2.val + rem
            val = curSum % 10
            rem = curSum //10
            cur.next = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        while l1:
            curSum = l1.val+ rem
            val = curSum % 10
            rem = curSum //10
            cur.next = ListNode(val)
            l1 = l1.next
            cur = cur.next
            
        while l2:
            curSum = l2.val+ rem
            val = curSum % 10
            rem = curSum //10
            cur.next = ListNode(val)
            l2 = l2.next
            cur = cur.next
        cur.next = ListNode(rem) if rem else None
        
        
        
            
        return dummy.next