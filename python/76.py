class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter

        if not s or not t:
            return ""

        target_counts = Counter(t)
        required_chars = len(target_counts)
        current_counts = Counter()

        left = 0
        min_len = float('inf')
        result = ""

        for right in range(len(s)):
            if s[right] in target_counts:
                current_counts[s[right]] += 1
                if current_counts[s[right]] == target_counts[s[right]]:
                    required_chars -= 1

            while required_chars == 0 and left <= right:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]

                if s[left] in target_counts:
                    current_counts[s[left]] -= 1
                    if current_counts[s[left]] < target_counts[s[left]]:
                        required_chars += 1

                left += 1

        return result
