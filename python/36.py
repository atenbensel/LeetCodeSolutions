class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num = board[i][j]
                box_idx = (i // 3) * 3 + ( j // 3)

                if num in rows[i] or num in cols[j] or num in boxes[box_idx]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)

        return True
