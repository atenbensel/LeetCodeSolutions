class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for num in nums [1:]:
            temp_max = max_product
            max_product = max(num, num * max_product, num * min_product)
            min_product = min(num, num * temp_max, num * min_product)
            result = max(result, max_product)

        return result
