class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                answer[i]= "fizzbuzz"
            elif i%5 == 0:
                answer[i] = "buzz"
            elif i%3 == 0:
                answer[i]= "fizz"
            else:
                answer[i]= str(i)
        return answer
            
            

