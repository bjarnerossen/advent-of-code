package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	content := string(data)

	// Split the input into rules and updates
	parts := strings.Split(content, "\n\n")
	rules := strings.Split(parts[0], "\n")
	updates := strings.Split(parts[1], "\n")

	// Parse the rules into a map of constraints
	constraints := make(map[int][]int)
	for _, rule := range rules {
		pair := strings.Split(rule, "|")
		from, _ := strconv.Atoi(pair[0])
		to, _ := strconv.Atoi(pair[1])
		constraints[from] = append(constraints[from], to)
	}
	// Process each update
	totalMiddleSum := 0
	for _, update := range updates {
		pages := parseUpdate(update)
		if isValidOrder(pages, constraints) {
			mid := findMiddlePage(pages)
			totalMiddleSum += mid
		}
	}

	fmt.Println("Sum of middle pages:", totalMiddleSum)
}

// parseUpdate converts a string update into a slice of integers
func parseUpdate(update string) []int {
	parts := strings.Split(update, ",")
	pages := make([]int, len(parts))
	for i, p := range parts {
		pages[i], _ = strconv.Atoi(p)
	}
	return pages
}

// isValidOrder checks if the order satisfies the constraints
func isValidOrder(pages []int, constraints map[int][]int) bool {
	// Create a quick lookup for page positions
	pos := make(map[int]int)
	for i, page := range pages {
		pos[page] = i
	}

	// Check each constraint
	for from, tos := range constraints {
		if posFrom, ok := pos[from]; ok {
			for _, to := range tos {
				if posTo, ok := pos[to]; ok {
					if posFrom > posTo {
						return false
					}
				}
			}
		}
	}
	return true
}

// findMiddlePage finds the middle page of a slice
func findMiddlePage(pages []int) int {
	mid := len(pages) / 2
	return pages[mid]
}
