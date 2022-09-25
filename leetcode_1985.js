/**
 * @param {string[]} nums
 * @param {number} k
 * @return {string}
 */
 var kthLargestNumber = function(nums, k) {
    
    nums.sort((x, y) => {
        
        if(Number(y) > Number.MAX_SAFE_INTEGER || Number(x) > Number.MAX_SAFE_INTEGER){
            
            return Number(BigInt(y) - BigInt(x))
            
        }
        
        return Number(y) - Number(x)
    
    })
    console.log(nums)
    
    return nums[k - 1]
    
};