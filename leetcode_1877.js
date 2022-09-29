/**
 * @param {number[]} nums
 * @return {number}
 */
 var minPairSum = function(nums) {
    
    nums.sort((x,y) => x - y)
    let max = 0
    
    let [left, right] = [0, nums.length-1]
    
    while(left < right){
        
        max = Math.max(max, nums[right] + nums[left])
        right--
        left++
    }
    
    return max
    
};