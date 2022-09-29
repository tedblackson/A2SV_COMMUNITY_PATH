/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function (nums, k) {

    nums.sort((x, y) => x - y)

    let [right, left, max] = [nums.length - 1, 0, 0]

    while (right > left) {

        if (nums[right] + nums[left] === k) {
            max++
            right--
            left++
        }
        else if (nums[right] + nums[left] > k) {
            right--
        }
        else {
            left++

        }

    }

    return max


};