# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge(list1, list2):
            cur1 = list1
            cur2 = list2
            merged = ListNode()
            current = merged
            while cur1 and cur2:
                if cur1.val <= cur2.val:
                    current.next = cur1
                    current = current.next
                    cur1 = cur1.next
                else:
                    current.next = cur2
                    current = current.next
                    cur2 = cur2.next
            
            current.next = cur1 or cur2
            return merged.next
            
        for i in range(len(lists) - 1):
            lists[i + 1] = merge(lists[i], lists[i + 1])
        return lists[-1] 