class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrack(i, j, k):
            if k == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] !=word[k]:
                return False

            original_chars = board[i][j]
            board[i][j] = '#'

            found = (backtrack(i + 1, j, k +1) or backtrack(i - 1, j, k + 1) or backtrack(i, j + 1, k + 1) or backtrack(i, j - 1, k + 1))

            board[i][j] = original_chars

            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False
