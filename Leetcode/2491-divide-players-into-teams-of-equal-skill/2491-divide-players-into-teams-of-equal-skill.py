class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = chemistry = 0
        total = skill[0] + skill[-1]
        right = len(skill) - 1
        
        while left <= right:
            
            if skill[left] + skill[right] != total:
                return -1
            else:
                chemistry += (skill[left] * skill[right])
            right -=1 
            left += 1
        return chemistry
                
            
            
            