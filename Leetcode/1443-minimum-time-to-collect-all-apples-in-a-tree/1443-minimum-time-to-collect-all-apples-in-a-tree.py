class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        visited = set()
        added = set()
                
        for src, dest in edges:
            tree[src].append(dest)
            tree[dest].append(src)
        
        def dfs(root):
            res = 0
            for child in tree[root]:
                if child not in visited:
                    visited.add(child)
                    res += dfs(child)
            return res + 2 if (hasApple[root]  or res ) and root != 0 else res
            
            
        visited.add(0)
        ans = dfs(0)

        return ans
        

            