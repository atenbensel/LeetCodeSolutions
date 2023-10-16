class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        stack = []
        n = len(heights)

        for i in range(n):
            start = i

            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                maxArea = max(maxArea, (i - index) * height)
                start = index

            stack.append((start, heights[i]))

        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, (n - index) * height)

        return maxArea
