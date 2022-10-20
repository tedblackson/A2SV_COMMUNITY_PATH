# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        length = 1
        current = node
        while current:
            length += 1
            current = current.next
        
        count = 1
        prev = node
        while node:
            if node.next:
                node.val = node.next.val
                prev = node
            
            if count == length - 1:
                prev.next = None
                
            node = node.next
            count += 1
            
            
        
        
        