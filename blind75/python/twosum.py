from collections import defaultdict

class Solution(object):
    def twoSum(self, nums, target):
        mapping = defaultdict(int)

        for index, val in enumerate(nums):
            diff = target - val
            if diff in mapping:
                return [index, mapping[diff]]
            else:
                mapping[val] = index
