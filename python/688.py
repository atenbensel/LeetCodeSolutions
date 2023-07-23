class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        dx = [2, 1, -1, -2, -2, -1, 1, 2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]

        dp = [[[0.0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1.0

        for moves in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for l in range(8):
                        x = i + dx[l]
                        y = j + dy[l]
                        if 0 <= x < n and 0 <= y < n:
                            dp[moves][i][j] += dp[moves - 1][x][y] / 8.0

        total_probability = sum(dp[k][i][j] for i in range(n) for j in range(n))
        return total_probability
