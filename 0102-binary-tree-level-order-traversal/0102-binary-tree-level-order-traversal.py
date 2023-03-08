# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            temp = []
            level = []
            while queue:
                cur = queue.popleft()
                if cur:
                    level.append(cur.val)
                    temp.append(cur.left) 
                    temp.append(cur.right)
            if level:
                ans.append(level) 
            queue = deque(temp)


        return ans

