class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(list)
        ans = [0]* n
        alpha = [0] * 26
        visited = set()
        for src , dest in edges:
            tree[src].append(dest)
            tree[dest].append(src)
        def combine(arr1, arr2):
            
            for i in range(26):
                arr1[i] += arr2[i]
            return arr1

        
        def dfs(root ):
        
            arr = [0] * 26
            idx = ord(labels[root]) - 97
            arr[idx] += 1
            for child in tree[root]:
                if child not in visited:
                    visited.add(child)
                    res = dfs(child)
                    combine(arr, res)
            ans[root] = arr[idx]
            return arr
            
        visited.add(0)
        dfs(0)
        return ans
