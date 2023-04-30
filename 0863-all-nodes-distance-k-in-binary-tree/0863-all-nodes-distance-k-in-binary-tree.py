# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(root):
            
            if not root:
                return
            if root.left:
                graph[root.left].append(root)
                graph[root].append(root.left)
            if root.right:
                graph[root.right].append(root)
                graph[root].append(root.right)

            dfs(root.left)
            dfs(root.right)
        dfs(root)
        queue = deque()
        queue.append(target)
        level = 0
        visited = set()
        visited.add(target)
        temp = []
        ans = []
        while queue:
            src = queue.popleft()
            if level == k:
                ans.append(src.val)
            for child in graph[src]:
                if child not in visited:
                    visited.add(child)
                    temp.append(child)
            if not queue and temp:
                queue = deque(temp)
                temp = []
                level += 1
        
        return ans