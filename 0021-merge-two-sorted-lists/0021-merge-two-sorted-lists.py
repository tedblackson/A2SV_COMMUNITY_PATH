# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        def solve(ans , node1, node2):
            if not (node1 and node2):
                ans.next = node1 or node2
                return 
            if node1.val <= node2.val:
                ans.next = node1
                solve(ans.next, node1.next, node2)
            else:
                ans.next = node2
                solve(ans.next, node1, node2.next)
        solve(ans, list1, list2)
        return ans.next                   
                