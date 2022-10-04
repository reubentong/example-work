from typing import List


# https://leetcode.com/problems/concatenation-of-array/
# https://leetcode.com/submissions/detail/814894266/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return list(nums + nums)


sol = Solution()
print(sol.getConcatenation([1, 2, 3, 4, 4, 4]))
