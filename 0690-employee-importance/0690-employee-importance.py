"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {}
        ans = [0]
        
        for employee in employees:
            graph[employee.id] = employee
        
        
        def dfs(node):
            
            ans[0] += node.importance
            
            for _id in node.subordinates:
                dfs(graph[_id])
        dfs(graph[id])
        return ans[0]
        