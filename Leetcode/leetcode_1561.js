/**
 * @param {number[]} piles
 * @return {number}
 */
 var maxCoins = function(piles) {
    
    let result = 0
    
    piles.sort((x,y) => x - y)
    
    let [right, left] = [piles.length-1,0]
    
    while(left < right - 1){
        
        result += piles[right - 1]
        
        
    
        right -=2
        left++
        
        
    }
    
    
    return result
    
    
    
};