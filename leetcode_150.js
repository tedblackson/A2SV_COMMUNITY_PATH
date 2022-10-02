/**
 * @param {string[]} tokens
 * @return {number}
 */
 var evalRPN = function(tokens) {
    
    
    let reversed = tokens.reverse()
    let tempStack = []
    
    let operators = {
        "+": function (num1, num2){ return num1 + num2},
        "-": function (num1, num2){return num2 - num1},
        "/" : function(num1, num2){ return num2/num1 < 0? Math.ceil(num2/num1) : Math.floor(num2/num1)},
        '*': function (num1, num2){ return num1 * num2}
    }
    
    while( reversed.length > 0){
        
        let current = reversed.pop()
        
        if(operators[current] != undefined){
            
            tempStack.push(operators[current](Number(tempStack.pop()), Number(tempStack.pop())))
            
        }
        
        else{
            tempStack.push(current)
        }
        
        
    }
    
    return tempStack.pop()
    
    
};