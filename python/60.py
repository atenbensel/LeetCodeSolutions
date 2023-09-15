class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            return num * factorial(num - 1)
        
        digits = list(map(str, range(1, n + 1)))
        k -= 1

        result = []
        
        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            index = k // fact
            k %= fact
            result.append(digits.pop(index))
        
        return ''.join(result)
