class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0

        a = list(a)
        b = list(b)

        while len(a) < len(b):
            a.insert(0, '0')
        while len(b) < len(a):
            b.insert(0, '0')

        for i in range(len(a) -1, -1, -1):
            bit_sum = int(a[i]) + int(b[i]) + carry
            carry = bit_sum // 2
            result.insert(0, str(bit_sum % 2))

        if carry > 0:
            result.insert(0, str(carry))

        return ''.join(result)
