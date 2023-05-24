# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(node1, node2):
            dummy = ListNode()
            cur = dummy
            while node1 and node2:
                if node1.val <= node2.val:
                    cur.next = node1
                    node1 = node1.next
                else:
                    cur.next = node2
                    node2 = node2.next
                cur = cur.next
                
            cur.next = node1 or node2
            return dummy.next
        return merge(list1, list2)              
                