# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_length = 0
        current_length = 0
        has_zero = False
        previous_length = 0

        for i in range(n):
            if nums[i] == 1:
                current_length += 1
                previous_length += 1
            else:
                has_zero = True
                max_length = max(max_length, current_length)
                current_length = previous_length
                previous_length = 0

        max_length = max(max_length, current_length)

        if has_zero:
            return max_length
        else:
            return max_length - 1 if max_length > 0 else 0
