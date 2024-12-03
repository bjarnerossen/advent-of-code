package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"regexp"
)

// Parse input data into a list of reports
func parseInput(input string) [][]int {
	lines := strings.Split(strings.TrimSpace(input), "\n")
	var memories [][]int

	for _, memory := range memories {
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
	memory := parseInput(string(input))

	fmt.Println(memory)
}