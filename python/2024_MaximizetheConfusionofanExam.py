class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        max_consecutive = 0
        max_count = 0
        counts = {'T': 0, 'F': 0}

        left = 0
        right = 0

        while right < len(answerKey):
            counts[answerKey[right]] += 1

            max_count = max(max_count, counts[answerKey[right]])

            if (right - left + 1) - max_count > k:
                counts[answerKey[left]] -= 1
                left += 1

            max_consecutive = max(max_consecutive, right - left + 1)

            right += 1

        return max_consecutive
        
