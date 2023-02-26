/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var rearrangeArray = function(nums) {
    
    let temp = []
    nums.sort((x, y) => x - y)
    let half = nums.length /2
    let median = nums.length%2 ?  nums[Math.floor(half)] : (nums[half - 1] + nums[half])/2

    
    let odd = 1
    let even = 0
    
    
    for(i = 0; i < nums.length ; i++  ){
        
        if(nums[i] < median){
            temp[odd] = nums[i]
            odd += 2
        }
        else{
            temp[even] = nums[i]
            even += 2
        }
    }
    
    return temp.filter(x => true)
};