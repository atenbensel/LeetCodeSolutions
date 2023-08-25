class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        while i >= 0  and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            left, right = i  + 1, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= nums[i]:
                    right = mid - 1
                else:
                    left = mid + 1
            nums[i], nums[left - 1] = nums[left - 1], nums[i]

        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
