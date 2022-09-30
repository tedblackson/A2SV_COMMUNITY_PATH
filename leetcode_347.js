/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
 var topKFrequent = function(nums, k) {
    
    let result = new Set()
    let counted = new Map()    
    for(let x of nums){
        
        if(counted.get(x) === undefined){
            counted.set(x, 1)
        }
        else{
            counted.set(x, counted.get(x)+1)
        }
    }
    
        nums.sort((x,y) => {
        
        return counted.get(y) - counted.get(x)
    })
    
    result = new Set(nums)
    result = [...result]
    

    
    
    return result.slice(0, k)
    
};