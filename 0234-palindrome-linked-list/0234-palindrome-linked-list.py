# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        cur = head
        
        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        if arr == list(reversed(arr)):
            return True
        else:
            return False
        
        
        
        
        
        
        
        
        
        