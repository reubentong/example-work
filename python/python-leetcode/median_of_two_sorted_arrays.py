# https://leetcode.com/problems/median-of-two-sorted-arrays/
# https://leetcode.com/submissions/detail/814227911/
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        listed = sorted(nums1 + nums2)
        listed_length = len(listed)
        if listed_length % 2 == 0:
            index_lower = listed[int(listed_length / 2 - 1)]
            index_upper = listed[int(listed_length / 2)]
            return (index_upper + index_lower) / 2
        else:
            return listed[int(listed_length / 2 - 0.5)]


sol = Solution()
print(sol.findMedianSortedArrays([1, 1], [1, 2]))
