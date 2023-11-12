# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        graph = defaultdict(list)
        self.buildGraph(root, None, graph)
        
        queue = deque((start,))
        visited = {start,}
        level = -1
        while queue:
            for _ in range(len(queue)):
                src = queue.popleft()
                
                for child in graph[src]:
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
            level += 1
            
        return level
                    
        
        

    
    def buildGraph(self, root, parent, graph):
        
        if not root:
            return
        
        if parent:
            graph[root.val].append(parent.val)
            graph[parent.val].append(root.val)
        
        

        
        self.buildGraph(root.left,root, graph)
        self.buildGraph(root.right, root, graph)
        
        
        