func maxSubArray(nums []int) int {
    maxSum := nums[0]
    currentSum := nums[0]

    for _, num := range nums[1:] {
        currentSum = max(num, currentSum+num)
        maxSum = max(maxSum, currentSum)
    }
    return maxSum
}
