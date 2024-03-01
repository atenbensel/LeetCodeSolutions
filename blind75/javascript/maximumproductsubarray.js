/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    if (nums.length === 0) return 0;

    let maxProduct = nums[0];
    let minProduct = nums[0];
    let result = nums[0];

    for (let i = 1; i < nums.length; i++) {
        let tempMax = maxProduct;
        maxProduct = Math.max(nums[i], nums[i] * maxProduct, nums[i] * minProduct);
        minProduct = Math.min(nums[i], nums[i] * tempMax, nums[i] * minProduct);
        result = Math.max(result, maxProduct);
    }
    return result;
};
