class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        
        length = 0
        
        for char in reversed(s):
            if char == ' ':
                break
            length += 1
        
        return length
