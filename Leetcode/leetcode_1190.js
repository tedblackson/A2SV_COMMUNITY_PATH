/**
 * @param {string} s
 * @return {string}
 */
 var reverseParentheses = function(s) {
    
    let stack = []
    let string = ""
    
    for(let i = 0; i < s.length; i++){
        
        if(s[i] === '('){
            stack.push(string)
            string = ""
        }
        else if(s[i]  === ')'){
            string = stack.pop() + [...string].reverse().join('')
        }
        else{
            string += s[i]
        }
    }
        
        return string
        
        
    };