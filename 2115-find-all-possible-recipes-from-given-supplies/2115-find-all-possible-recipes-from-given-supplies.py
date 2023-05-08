class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        queue = deque()
        order = []
        indegrees = defaultdict(int)
        graph = defaultdict(list)
        
        for i in range(len(ingredients)):
            child = recipes[i]
            for parent in ingredients[i]:
                graph[parent].append(child)
                if parent not in supplies:
                    indegrees[child] += 1
        print
            
        
        for recipe in recipes:
            if not indegrees[recipe]:
                queue.append(recipe)
        
        
        while queue:
            current = queue.popleft()
            order.append(current)
            
            for child in graph[current]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)
        
        return order
                
            
            
            
            