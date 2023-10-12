class MapSum:

    def __init__(self):
        self.root = [0] * 27
        self.tot = 0
    
        
        

    def insert(self, key: str, val: int) -> None:
        cur = self.root

        for char in key:
            idx = ord(char) - ord('a')
            if not cur[idx]:
                cur[idx] = [0] * 27
            cur = cur[idx]
        cur[26] = val

        

    def sum(self, prefix: str) -> int:
        cur = self.root
        self.tot = 0
        for char in prefix:
            idx = ord(char) - ord('a')  
            
            if not cur[idx]:
                return 0
            cur = cur[idx]
        
        self.dfs(cur)
        return self.tot
    
    def dfs(self, root):
        self.tot += root[26]
        for child in root:
            if type(child) != int and child:
                self.dfs(child)
            




# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)