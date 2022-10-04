package main

import "fmt"

//https://leetcode.com/problems/two-sum/
//https://leetcode.com/submissions/detail/814968455/

func main() {
	fmt.Println(twoSum([]int{3, 3}, 6))
}

func twoSum(nums []int, target int) []int {
	dict := make(map[int]int)
	for i, number := range nums {
		j, ok := dict[number]
		if ok {
			return []int{j, i}
		}
		dict[target-number] = i
	}
	return []int{}
}
