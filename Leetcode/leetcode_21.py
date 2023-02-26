# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not list1:
            return list2
        if not list2:
            return list1
        
        head = list1 if list1.val <= list2.val else list2
        
        cur1 = list1
        cur2 = list2
        
        if head is list1:
            cur1 = cur1.next
        else:
            cur2 = cur2.next
            
        current = head
            
        while cur1 or cur2:
            
            if not cur1 :
                current.next = cur2
                return head
            elif not cur2:
                current.next = cur1
                return head
            if cur1.val <= cur2.val:
                current.next = cur1
                cur1 = cur1.next
            else:
                current.next = cur2
                cur2 = cur2.next
            current = current.next
        return head
            
        