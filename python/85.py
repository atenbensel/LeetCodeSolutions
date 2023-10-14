class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        currRow = [0] * m
        max_area = 0

        def histogram(heights):
            st1 = []
            st2 = []
            left = [0] * len(heights)
            right = [0] * len(heights)

            # Previous smaller element
            for i in range(len(heights)):
                num = heights[i]

                while st1 and heights[st1[-1]] > num:
                    st1.pop()

                if not st1:
                    left[i] = -1
                else:
                    left[i] = st1[-1]

                st1.append(i)

            # Next greater element
            for i in range(len(heights) - 1, -1, -1):
                num = heights[i]

                while st2 and heights[st2[-1]] >= num:
                    st2.pop()

                if not st2:
                    right[i] = len(heights)
                else:
                    right[i] = st2[-1]

                st2.append(i)

            max_rect = 0
            for i in range(len(heights)):
                area = (right[i] - left[i] - 1) * heights[i]
                max_rect = max(max_rect, area)

            return max_rect

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    currRow[j] += 1
                else:
                    currRow[j] = 0

            curr_max = histogram(currRow)
            max_area = max(max_area, curr_max)

        return max_area
