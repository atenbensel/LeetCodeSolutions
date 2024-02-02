func twoSum(nums []int, target int) []int {
    numMap := make(map[int]int)
    for i, num := range nums {
        complement := target - num
        if index, ok := numMap[complement]; ok {
            return []int{index, i}
        }
        numMap[num] = i
    }
    return nil
}
