class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        n = len(weights)
        pairWeights = []

        for i in range(1, n):
            pairWeights.append(weights[i] + weights[i -1])

        pairWeights.sort()

        max_score = sum(pairWeights[n - k:])

        min_score = sum(pairWeights[:k - 1])

        return max_score - min_score
