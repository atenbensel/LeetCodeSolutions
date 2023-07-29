class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        def help(a, b, mp):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            if (a, b) in mp:
                return mp[(a, b)]

            ans = 0
            ans += help(a - 100, b, mp)
            ans += help(a - 75, b - 25, mp)
            ans += help(a - 50, b - 50, mp)
            ans += help(a - 25, b - 75, mp)

            mp[(a, b)] = ans / 4.0
            return mp[(a, b)]

        if n >= 4800:
            return 1.0

        mp = {}
        return help(n, n, mp)
