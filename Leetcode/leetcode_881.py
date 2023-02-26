class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left = count = 0
        right = len(people) -1
        people.sort()
        
        while left <= right:
            print(people[left], people[right])
            if people[right] + people[left] <= limit:
                left += 1
            right -= 1
            count += 1
        return count