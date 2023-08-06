class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        
        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j - 1] * (n - j + 1)) % MOD
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD
        
        return dp[goal][n]
