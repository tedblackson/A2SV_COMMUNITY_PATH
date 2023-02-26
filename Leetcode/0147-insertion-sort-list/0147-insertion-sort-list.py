# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 0
        cur = head
        
        while cur:
            length += 1
            cur = cur.next
        cur1 = head
        for i in range(length):
            
            cur2 = head
            for _ in range(i):
                
                if cur1.val < cur2.val:
                    cur2.val, cur1.val = cur1.val , cur2.val
                
                cur2 = cur2.next
            cur1 = cur1.next
            
        return head
            
        
                
                

        



        
        

                

            

            

                






