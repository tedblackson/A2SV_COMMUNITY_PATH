/**
 * @param {number[]} arr
 * @return {number[]}
 */
var pancakeSort = function(arr) {
    
    
    let [left, right] = [0,arr.length -1]
    let result = []
    
    while(left <= right){
        
        
        let maxIndex = 0;
        let max = 0
        
        for(let i = 0; i <= right; i++){
            
            if(max < arr[i]){
                max = arr[i]
                maxIndex = i
            }
            

            
        }
        
        
        if(maxIndex === left){
            result.push(right+1)
            arr = [...arr.slice(left, right + 1).reverse(), ...arr.slice(right+1, arr.length)]
            
            right--
            
        }
        else if(maxIndex === right){
        
            right--
            continue
        }
        
        else{
            result.push(maxIndex + 1)
            arr = [...arr.slice(left, maxIndex + 1).reverse(), ...arr.slice(maxIndex + 1, arr.length)]
        }
    }
    
    
    return result
    
    
    

    
};