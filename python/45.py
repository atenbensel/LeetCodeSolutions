class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0

        jumps = 0
        current_max = 0
        next_max = 0

        for i in range(n):
            if i > current_max:
                jumps += 1
                current_max = next_max

            next_max = max(next_max, i  + nums[i])

            if current_max >= n - 1:
                break

        return jumps
