class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def pow_helper(x, n):
            if n == 0:
                return 1.0
            
            half_pow = pow_helper(x, n // 2)

            if n % 2 == 0:
                return half_pow * half_pow
            else:
                return half_pow * half_pow * x

        if n < 0:
            x = 1 / x
            n = -n
        
        return pow_helper(x, n)
