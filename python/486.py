class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                choose_left = nums[left] - dp[left + 1][right]
                choose_right = nums[right] - dp[left][right - 1]
                dp[left][right] = max(choose_left, choose_right)

        return dp[0][n - 1] >= 0
