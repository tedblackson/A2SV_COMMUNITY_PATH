# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        even = head.next if head else None
        segment = even

        while odd and even:
            odd.next = odd.next.next if odd.next and odd.next.next else segment
            odd = odd.next
            even.next = even.next.next if even.next and even.next.next else None
            even = even.next
        if odd is not segment:
            odd.next = segment
        
        return head

