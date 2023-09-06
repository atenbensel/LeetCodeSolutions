class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_valid(queens, row, col):
            for r, c in queens:
                if c == col or abs(row - r) == abs(col - c):
                    return False
            return True

        def solve(queens, row):
            if row == n:
                self.count += 1
                return
            for col in range(n):
                if is_valid(queens, row, col):
                    queens.append((row, col))
                    solve(queens, row + 1)
                    queens.pop()

        self.count = 0
        queens = []
        solve(queens, 0)
        return self.count
