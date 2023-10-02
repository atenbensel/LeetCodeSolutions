class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = bin(int(a, 2) + int(b, 2))

        return result[2:]
