class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (1 << n)

        for i in range( 1 << n):
            ans[i] = i ^  (i >> 1)

        return ans
