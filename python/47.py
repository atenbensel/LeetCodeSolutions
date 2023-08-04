class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
            
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        backtrack(0)
        return result
