class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_bound(nums, target, is_first):
            left, right = 0, len(nums)
            while  left < right:
                mid = left + (right - left) // 2
                if (is_first and nums[mid] >= target) or (not is_first and nums[mid] > target):
                    right = mid
                else:
                    left = mid + 1
            return left

        left_idx = find_bound(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        right_idx = find_bound(nums, target, False) - 1

        return [left_idx, right_idx]
