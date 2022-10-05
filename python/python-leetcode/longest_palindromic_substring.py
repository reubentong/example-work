# https://leetcode.com/problems/longest-palindromic-substring/
# https://leetcode.com/submissions/detail/815614569/ #TODO Too slow


# loop through substrings # reverse string
# check if reverse ==  and save longest

class Solution: 
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        all_subs = list(s[i:j + 1] for i in range(len(s)) for j in range(i, len(s)))
        for i in all_subs:
            if i[::-1] == i and len(i[::-1]) > len(longest):
                longest = i[::-1]
        return longest


sol = Solution()
print(sol.longestPalindrome(s="hello"))
