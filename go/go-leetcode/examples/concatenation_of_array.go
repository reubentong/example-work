package main

import "fmt"

//https://leetcode.com/problems/concatenation-of-array/
//https://leetcode.com/submissions/detail/814888760/

func main() {
	fmt.Println(getConcatenation([]int{1, 2, 3}))
}

func getConcatenation(nums []int) []int {
	return append(nums, nums...)
}
