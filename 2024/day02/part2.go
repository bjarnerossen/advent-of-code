package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isSafe(report []int) bool {
	if len(report) < 2 {
		return false
	}

	isValid := func(arr []int) bool {
		if len(arr) < 2 {
			return false
		}

		isIncreasing := true
		isDecreasing := true

		for i := 1; i < len(arr); i++ {
			diff := arr[i] - arr[i-1]

			// Check if the difference is within range
			if diff < -3 || diff > 3 || diff == 0 {
				return false
			}

			// Determine if it's increasing or decreasing
			if diff < 0 {
				isIncreasing = false
			} else {
				isDecreasing = false
			}
		}

		// A report is safe if it's strictly increasing or strictly decreasing
		return isIncreasing || isDecreasing
	}

	// Check if the original report is valid
	if isValid(report) {
		return true
	}

	// Try removing each level and check the modified report
	for i := 0; i < len(report); i++ {
		// Create a new slice by removing the i-th element
		modifiedReport := make([]int, len(report)-1)
		copy(modifiedReport[:i], report[:i])
		copy(modifiedReport[i:], report[i+1:])

		// If the modifiedReport is now safe, then return true
		if isValid(modifiedReport) {
			return true
		}
	}

	// If no modification works, return false
	return false
}

// Parse input data into a list of reports
func parseInput(input string) [][]int {
	lines := strings.Split(strings.TrimSpace(input), "\n")
	var reports [][]int

	for _, line := range lines {
		parts := strings.Fields(line)
		var report []int
		for _, part := range parts {
			num, err := strconv.Atoi(part)
			if err != nil {
				fmt.Println("Error parsing number:", err)
				continue
			}
			report = append(report, num)
		}
		reports = append(reports, report)
	}

	return reports
}

func main() {
	input, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// Parse input into reports
	reports := parseInput(string(input))

	// Count safe reports
	safeCount := 0
	for _, report := range reports {
		if isSafe(report) {
			safeCount++
		}
	}

	fmt.Println("Number of safe reports:", safeCount)
}
