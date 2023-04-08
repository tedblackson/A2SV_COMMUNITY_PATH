# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
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
        
        def mid(node):
            slow = fast = node
            
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def cut(node, middle):
            
            while node and node.next != middle:
                node = node.next
            node.next = None
            
            
        def mergeSort(node):
            if not node or not node.next:
                return node
            
            middle = mid(node)
            cut(node, middle)
            
            node = mergeSort(node)
            middle = mergeSort(middle)              
            return merge(node, middle)
            
        ans = mergeSort(head)
        return ans
            
            
            