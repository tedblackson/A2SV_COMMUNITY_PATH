# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root, parent):
            if not root:
                return
            
            if parent:
                root.parent = parent
            
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root, None)
        queue, visited = deque(), set()
        queue.append(target)
        visited.add(target)
        ans, temp, level = [], [], 0
            
        while queue:
            src = queue.popleft()
            
            if src:
                if level == k:
                    ans.append(src.val)
                children = [src.left, src.right]
                if src != root:
                    children.append(src.parent)
                
                for child in children:
                    if child not in visited:
                        visited.add(child)
                        temp.append(child)
            if not queue and temp:
                queue = deque(temp)
                temp = []
                level +=1
        return ans
                
        
        
        
        