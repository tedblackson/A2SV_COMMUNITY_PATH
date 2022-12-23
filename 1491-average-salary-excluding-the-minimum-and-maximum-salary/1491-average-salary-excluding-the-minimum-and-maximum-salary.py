class Solution:
    def average(self, salary: List[int]) -> float:

        maximum = max(salary)
        minimum = min(salary)
        total = sum(salary)

        return (total - maximum - minimum )/(len(salary) - 2)