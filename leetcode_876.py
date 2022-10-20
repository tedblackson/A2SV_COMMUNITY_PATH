# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        count = 1
        res = 0
        
        if not cur.next:
            return cur
        while cur.next  :
            count += 1
            cur = cur.next
        
        res =  count /2 + 1 if  count%2 == 0  else ceil(count /2)
        
        cur = head
        count = 1
        if res ==2:
            return cur.next
        while cur.next:
            if count == res:
                return cur
            count += 1
            cur = cur.next
            
            