# https://leetcode.com/problems/two-sum/
# https://leetcode.com/submissions/detail/814283724/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] in dictionary:
                return [dictionary[nums[i]], i]
            else:
                dictionary[target - nums[i]] = i


sol = Solution()
print(sol.twoSum([3, 3], 6))
