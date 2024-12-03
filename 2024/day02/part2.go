package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Checks if a report is safe
func isSafe(report []int) bool {
	if len(report) < 2 {
		return false
	}

	isIncreasing := true
	isDecreasing := true

	// First check if the report is already safe
	for i := 1; i < len(report); i++ {
		diff := report[i] - report[i-1]

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
	if isIncreasing || isDecreasing {
		return true
	}

	// If the report is not safe, try removing one level at a time
	for i := 0; i < len(report); i++ {
		modifiedReport := append(report[:i], report[i+1:]...)
		fmt.Println(modifiedReport)
		if isSafe(modifiedReport) {
			return true // The modified report is safe
		}
	}
	return false // No modifications lead to a safe report
}

// func isSafeWithProblemDampener(report []int) bool {
// }

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
