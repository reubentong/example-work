# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# https://leetcode.com/submissions/detail/814252380/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_found = {}
        max_length = 0
        window_start = 0
        for element in range(len(s)):
            if s[element] not in char_found:
                char_found[s[element]] = element
            else:
                while s[element] in char_found:
                    del char_found[s[window_start]]
                    window_start += 1
                char_found[s[element]] = element
            max_length = max(max_length, element - window_start + 1)
        return max_length


sol = Solution()
print(sol.lengthOfLongestSubstring(s="roaafkte"))
