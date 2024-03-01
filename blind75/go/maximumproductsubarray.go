func maxProduct(nums []int) int {
    if len(nums) == 0 {
        return 0
    }

    maxProduct := nums[0]
    minProduct := nums[0]
    result := nums[0]

    for i := 1; i < len(nums); i++ {
        tempMax := maxProduct
        maxProduct = max(nums[i], max(nums[i]*maxProduct, nums[i]*minProduct))
        minProduct = min(nums[i], min(nums[i]*tempMax, nums[i]*minProduct))
        result = max(result, maxProduct)
    }
    return result
}
