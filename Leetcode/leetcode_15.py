# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        queue = []
        
        def check(head):
            queue.append(head.val)
            if head.next == None:
                return head.val == queue.pop(0)
            return  check(head.next) and head.val == queue.pop(0)
        return check(head)
        
        
        