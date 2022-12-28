class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        visited = defaultdict(list)
        ans = []
        
        for directory in paths:
            
            files = directory.split()
            root = files[0]
            for file in files[1:]:
                temp = file.split('(')
                content = temp[1][:len(temp[1]) - 1]
                visited[content].append(root + '/' + temp[0])
        ans = list(filter( lambda x : len(x) > 1, visited.values()))
        return ans
            
        
            
        