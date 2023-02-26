class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        real1, complex1 = num1.split('+')
        real2, complex2 = num2.split('+')
        ansReal = int(real1) * int(real2)
        ansComplex = str( int(real2) * int(complex1[:-1]) + int(real1) * int(complex2[:-1]))
        ansNegative = -1 * int(complex1[:-1]) * int(complex2[:-1])
        
        ans = str(ansReal + ansNegative)+ "+" + ansComplex + 'i'
        return ans
        