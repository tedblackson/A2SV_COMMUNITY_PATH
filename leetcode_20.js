/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = []
    
    let opening= new Map([['(', ')'], ['[',']'], ['{', '}']])
    
   
        

    
    for(let x of s){
        
        if(opening.has(x)){
            stack.push(x)
        }
        
        
        else{
            if(x === opening.get(stack[stack.length - 1])){
                    stack.pop()
            }
            else{
                return false
            }
        }
    }
    
    if(stack.length !== 0){
        return false
    }
    return true
    
};