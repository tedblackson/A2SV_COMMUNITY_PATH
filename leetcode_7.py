class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            return x * self.myPow(x * x, n//2) if n%2 else self.myPow(x * x,n//2)
        