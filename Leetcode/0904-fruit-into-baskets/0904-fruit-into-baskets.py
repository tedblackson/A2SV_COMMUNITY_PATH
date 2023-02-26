class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        visited = defaultdict(int)
        start = 0
        maximum = 0
        for end in range(len(fruits)):
            visited[fruits[end]] += 1           
            while len(visited) > 2:
                visited[fruits[start]] -= 1
                if not visited[fruits[start]]:
                    del visited[fruits[start]]
                start += 1
            if len(visited) <= 2:
                maximum = max(maximum, end - start + 1)
        return maximum
