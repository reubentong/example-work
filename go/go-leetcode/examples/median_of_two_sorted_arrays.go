package main

import (
	"fmt"
	"sort"
)

//https://leetcode.com/problems/median-of-two-sorted-arrays/
//https://leetcode.com/submissions/detail/814924203/

func main() {
	fmt.Println(findMedianSortedArrays([]int{1, 2}, []int{3, 4}))
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	sortedList := append(nums1, nums2...)
	sort.Ints(sortedList)
	length := len(sortedList)
	if length%2 == 0 {
		indexLower := float64(sortedList[length/2-1])
		indexUpper := float64(sortedList[length/2])
		return (indexLower + indexUpper) / 2
	} else {
		index := float64(length)/2 - .5
		return float64(sortedList[int(index)])
	}
}
