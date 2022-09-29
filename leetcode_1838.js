/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxFrequency = function(nums, k) {
    
    nums.sort((x,y) => x - y)
    
    let [right, left, total,max] = [0,0, 0, 0]
    
    
    while(right < nums.length){
        
        total += nums[right]
        
        while((nums[right] * (right - left + 1)) > total + k){
            
            total-= nums[left]
            left++

            
        }

        
        max = Math.max(max, right - left + 1)
        right++

        
    }
    
    return max
    
    
};