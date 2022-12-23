class Solution:
    def interpret(self, command: str) -> str:

        map = {'()' : "o", '(al)' : 'al'}

        ctr = 0
        newS = ''
        while ctr < len(command):
            if command[ctr] == '(':
                if command[ctr +1] == ')':
                    newS += "o"
                    ctr += 2
                elif command[ctr + 1] == 'a':
                    newS += 'al'
                    ctr+=4
                
            elif command[ctr] == 'G':
                newS += 'G'
                ctr +=1
        return newS
            
