# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        cur = head
        hashmap = defaultdict(deque)
        
        stack = []
        
        while cur:
            
            while stack and stack[-1].val< cur.val:
                hashmap[stack.pop()].append(cur.val)
            stack.append(cur)
            cur = cur.next
        cur = head
        output = []
        while cur:
        
            output.append(hashmap[cur].popleft()) if hashmap[cur] else output.append(0)
            cur = cur.next
        return output
            
            
                