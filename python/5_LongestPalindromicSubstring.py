# Question:
# Given a string s, return the longest palindromic substring in s.

# Solution:

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expand(s, left, right):
        	while left >= 0 and right < len(s) and s[left] == s[right]:
        		left -= 1
        		right += 1
        	return right-left-1

        start, end = 0, 0
        for index in range(len(s)):
        	even_len = expand(s, index, index+1)
        	odd_len = expand(s, index, index)
        	length = max(even_len, odd_len)
        	if length > (end-start):
        		start = index - (length-1)/2
        		end = index +length/2

        return s[start:end+1]
      
