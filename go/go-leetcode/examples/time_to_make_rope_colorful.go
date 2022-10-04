package main

import "fmt"

//https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
//https://leetcode.com/submissions/detail/814855059/
//loop through letters
// if colour [i] = colour - 1 [i-1] get the time [i]
// add all time

func main() {
	colors := "abbabba"
	neededTime := []int{1, 2, 3, 2, 6, 7, 2}
	fmt.Println(minCost(colors, neededTime))
}

func minCost(colors string, neededTime []int) int {
	var time int
	for i := 0; i < len(colors)-1; i++ {
		if colors[i] != colors[i+1] {
			continue
		}
		if neededTime[i] > neededTime[i+1] {
			neededTime[i], neededTime[i+1] = neededTime[i+1], neededTime[i]
		}
		time += neededTime[i]
	}
	return time
}
