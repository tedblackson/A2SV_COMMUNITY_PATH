# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        pos = 1

        current = head

        while current:
            if pos == length - n :
                current.next = current.next.next
            elif length - n == 0:
                head = head.next
                break
            pos += 1
            current = current.next
        return head


