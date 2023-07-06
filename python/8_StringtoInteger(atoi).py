class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()

        if len(s) == 0:
            return 0

        if s[0] == '+' or s[0] == '-':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        else:
            sign = 1

        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                break
        
        num *= sign
        num = max(min(num, 2**31 - 1), -2**31)

        return num
