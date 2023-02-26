/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
 var sortColors = function(nums) {
    
    for(let i = 0; i < nums.length; i++){
        
        let smallest =  nums[i]
        let index ;
        
        for(let j = i+1; j < nums.length; j++){
            if (nums[j] < smallest){
                smallest = nums[j]
                index = j
            }
        }
        
        [nums[i], nums[index]] = [smallest, nums[i]]
    }
    
    
};