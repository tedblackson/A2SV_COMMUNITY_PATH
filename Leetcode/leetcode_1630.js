/**
 * @param {number[]} nums
 * @param {number[]} l
 * @param {number[]} r
 * @return {boolean[]}
 */
 var checkArithmeticSubarrays = function(nums, l, r) {
    
    
    let result = []
    
    for(let i in l){
        
        let temp = [...nums.slice(l[i], r[i]+1)]
        temp.sort((x, y)=> x - y)
        
        let final = true
        let gap = temp[1] - temp[0]
       
        
        for(let j = 0; j < temp.length - 1; j++){
            
            
            if(temp[j + 1] - temp[j] !== gap){
                final = false    
            }
            
        }
        
        result.push(final)
        
        
        
        
    }
    
    return result
};