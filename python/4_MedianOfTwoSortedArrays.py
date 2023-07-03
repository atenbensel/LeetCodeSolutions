# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Solution:
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        total_length = m + n
        median = 0

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (total_length + 1) // 2 - partition1

            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if total_length % 2 == 0:
                    median = (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                else:
                    median = max(maxLeft1, maxLeft2)
                break

            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1

        return median
