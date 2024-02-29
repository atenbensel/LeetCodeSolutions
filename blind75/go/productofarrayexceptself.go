func productExceptSelf(nums []int) []int {
    length := len(nums)
    answer := make([]int, length)
    answer[0] = 1
    for i := 1; i < length; i++ {
        answer[i] = nums[i-1] * answer[i-1]
    }
    R := 1
    for i := length - 1; i >= 0; i-- {
        answer[i] = answer[i] * R
        R *= nums[i]
    }
    return answer
}
