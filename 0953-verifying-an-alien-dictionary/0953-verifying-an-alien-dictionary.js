/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
var isAlienSorted = function(words, order) {
    mapper = {}
    for (let i = 0; i < order.length ; i++) mapper[order[i]] = i;
    
    original = [...words]
    
    words.sort( (first, second) => {
               
                small = Math.min(first.length, second.length)
    
                for(let i = 0; i < small; i++){
                        if (first[i]  !== second[i]){
                            return   mapper[first[i]] - mapper[second[i]] 
                        }       
                }
                    
                return first.length - second.length 
               })
    return words.every((val, idx) => val == original[idx])
               
    
    
    
};