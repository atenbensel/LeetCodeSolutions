from collections import Counter

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def helper(s1, s2, memo):
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            if Counter(s1) != Counter(s2):
                memo[(s1, s2)] = False
            elif s1 == s2:
                memo[(s1, s2)] = True
            else:
                for k in range(1, len(s1)):
                    if (helper(s1[k:], s2[k:], memo) and helper(s1[:k], s2[:k], memo)) or \
                       (helper(s1[k:], s2[:-k], memo) and helper(s1[:k], s2[-k:], memo)):
                        memo[(s1, s2)] = True
                        break
                else:
                    memo[(s1, s2)] = False
            return memo[(s1, s2)]

        memo = {}
        return helper(s1, s2, memo)
