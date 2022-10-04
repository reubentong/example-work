# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
# https://leetcode.com/submissions/detail/814948749/
from typing import List


# loop through str, if != one after ignore,
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        for i in range(len(colors) - 1):
            if colors[i] != colors[i + 1]:
                continue
            if neededTime[i] > neededTime[i + 1]:
                neededTime[i], neededTime[i + 1] = neededTime[i + 1], neededTime[i]
            time += neededTime[i]
        return time


sol = Solution()
print(sol.minCost("abbabba", [1, 2, 3, 2, 6, 7, 2]))
