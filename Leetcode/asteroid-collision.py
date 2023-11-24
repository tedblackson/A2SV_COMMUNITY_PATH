class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for asteroid in asteroids:
            
            cur = asteroid
            flag = False
            while stack and (  (stack[-1] > 0 and cur < 0)):
                last = stack.pop()
                if abs(last) > abs(asteroid):
                    cur = last
                elif abs(last) == abs(asteroid):
                    flag = True
                    break
            if not flag:
                stack.append(cur)
        return stack