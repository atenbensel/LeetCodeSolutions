class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            turns = dp(i + 1, j) + 1
            
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    turns = min(turns, dp(i, k - 1) + dp(k + 1, j))
            
            memo[(i, j)] = turns
            return turns
        
        n = len(s)
        if n == 0:
            return 0
        
        memo = {}
        return dp(0, n - 1)
