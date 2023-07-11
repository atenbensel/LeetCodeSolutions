class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        combinations = []

        def backtrack(s, left, right):
            if left == 0 and right == 0:
                combinations.append(s)
                return

            if left > 0:
                backtrack(s + '(', left - 1, right)

            if right > left:
                backtrack(s + ')', left, right - 1)
            
        backtrack('', n, n)

        return combinations
