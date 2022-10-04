package main

import "fmt"

//https://leetcode.com/problems/two-sum/

func main() {
	fmt.Println(twoSum)
}

func twoSum(nums []int, target int) []int {
	var loopA = nums
	var loopB = nums
	var myslice []int
	for i := range loopA {
		intA := loopA[i]
		for index := range loopB {
			intB := loopB[index]
			if intA+intB == target {
				if len(myslice) < 2 {
					myslice = append(myslice, i)
					myslice = append(myslice, index)
				}
			}
		}
	}
	return myslice
}
