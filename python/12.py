class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        roman_numeral = ""
        i = 0

        while num > 0:
            if num >= values[i]:
                roman_numeral += symbols[i]
                num -= values[i]
            else:
                i += 1
        
        return roman_numeral
