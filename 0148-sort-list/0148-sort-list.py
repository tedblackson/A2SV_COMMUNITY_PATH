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
            slow = node
            fast = node.next
            
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        # def cut(node, middle):
        #     while node and node.next != middle:
        #         node = node.next
        #     node.next = None
            
            
        def mergeSort(node):
            if not node or not node.next:
                return node
            first= node
            second = mid(node)
    
            temp = second.next
            second.next = None
            second = temp
            
            first = mergeSort(first)
            second = mergeSort(second)              
            return merge(first, second)
            
        ans = mergeSort(head)
        return ans
            
            
            