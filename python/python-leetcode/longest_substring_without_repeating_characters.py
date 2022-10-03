# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        current = ""
        if len(s) <= 1:
            return len(s)
        else:
            for element in range(0, len(s)):
                print(longest)
                if s[element] not in current:
                    current = current + s[element]
                if element + 1 < len(s) and s[element + 1] in current:
                    if len(current) > len(longest):
                        longest = current
                        current = ""
                    return len(longest)


sol = Solution()
print(sol.lengthOfLongestSubstring(s="roach"))
