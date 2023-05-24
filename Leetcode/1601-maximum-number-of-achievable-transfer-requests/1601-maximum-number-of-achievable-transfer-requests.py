class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        net = [0] * n
        ans = [0]

        def isBalanced(arr):
            for ele in arr:
                if ele != 0:
                    return False
            return True
        
        
        def backtrack(start, count):
            if isBalanced(net):
                ans[0] = max(ans[0], count)
            if start >= len(requests):
                
                return
            
            request = requests[start]
            net[request[0]] -=1
            net[request[1]] += 1
            backtrack(start + 1, count +1)
            net[request[0]] += 1
            net[request[1]] -= 1
            backtrack(start + 1, count)
        backtrack(0, 0)
        return ans[0]
                