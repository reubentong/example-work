package main

import (
	"fmt"
)

//https://leetcode.com/problems/concatenation-of-array/
//https://leetcode.com/submissions/detail/814913579/

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb"))
}

func lengthOfLongestSubstring(s string) int {
	mapped, maxLength, left := make(map[rune]int), 0, 0
	for i, current := range s {
		if val, okay := mapped[current]; okay == true && val >= left {
			if i-left > maxLength {
				maxLength = i - left
			}
			left = val + 1
		}
		mapped[current] = i
	}
	if len(s)-left > maxLength {
		maxLength = len(s) - left
	}
	return maxLength
}
