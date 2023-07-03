# QUESTION: 
# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

# Solution:

class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False

        if s == goal:
            char_counts = [0] * 26
            for char in s:
                char_counts[ord(char) - ord('a')] += 1
            return any(count >= 2 for count in char_counts)

        differences = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                differences.append(i)

        return len(differences) == 2 and s[differences[0]] == goal[differences[1]] and s[differences[1]] == goal[differences[0]]
