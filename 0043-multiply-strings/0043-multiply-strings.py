class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        newNum1 = 0
        newNum2 = 0
        for ele in num1:
            newNum1 = newNum1 * 10  + int(ele)
            
        for ele in num2:
            newNum2 = newNum2 * 10 + int(ele)
        
        return str(newNum1 * newNum2)
            


       
                    

                


        

        
