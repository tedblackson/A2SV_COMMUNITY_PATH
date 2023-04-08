# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        
        def reverse(head):
            cur = head
            prev = None
            
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        
        right_cut = left_cut = None
        
        cur = head
        count = 1
        while cur and cur.next:
            if count == left - 1:
                left_cut = cur
                
            if count == right:
                right_cut = cur.next
                cur.next = None
            cur = cur.next if cur else None
            count +=1 
        temp = None
       
        
        if left == 1:
            temp = head
            head = reverse(head)
        elif left_cut:
            temp = left_cut.next
            left_cut.next = reverse(left_cut.next)
        if temp and right_cut:   
            temp.next = right_cut
        return head
        
        
            
        
        