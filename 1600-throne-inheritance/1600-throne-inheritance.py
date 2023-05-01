class ThroneInheritance:
    

    def __init__(self, kingName: str):
        self.tree = defaultdict(deque)
        self.king = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.tree[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead.add(name)
        
        
        

    def getInheritanceOrder(self) -> List[str]:
        inheritance = []
        def dfs(root):
            if root not in self.dead:
                inheritance.append(root)
            
            for child in self.tree[root]:
                dfs(child)
        dfs(self.king)
        return inheritance
                
            
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()