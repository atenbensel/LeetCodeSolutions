class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows

        current_row = 0
        direction = -1

        for char in s:
            rows[current_row] += char

            if current_row == 0 or current_row == numRows - 1:
                direction *= -1

            current_row += direction

        return ''.join(rows)
