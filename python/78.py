class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start, current_subset):
            if start == len(nums):
                subsets.append(current_subset[:])
                return

            current_subset.append(nums[start])
            backtrack(start + 1, current_subset)

            current_subset.pop()
            backtrack( start + 1, current_subset)

        subsets = []
        backtrack(0, [])
        return subsets
