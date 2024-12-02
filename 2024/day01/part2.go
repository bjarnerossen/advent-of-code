package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var answer int
	var left, right []int

	input, err := os.ReadFile("input.txt") // Read input file
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// Parse the output into left and right slices
	scanner := bufio.NewScanner(bytes.NewReader(input)) // Create a scanner to read from the input
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)

		if len(parts) == 2 {
			l, err := strconv.Atoi(parts[0])
			if err != nil {
				fmt.Println("Error converting left part:", err)
				continue
			}
			r, err := strconv.Atoi(parts[1])
			if err != nil {
				fmt.Println("Error converting right part:", err)
				continue
			}

			// Append to the left and right slices
			left = append(left, l)
			right = append(right, r)
		}
	}

	// Handle errors from scanner
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading input:", err)
		return
	}

	// Count occurrences of each number in the right list
	countMap := make(map[int]int)
	for _, num := range right {
		countMap[num]++
	}
	
	// Calculate the similarity score
	for _, num := range left {
		answer += num * countMap[num] // Multiply by the count of num in the right list
	}
	
	// Print the total similarity score
	fmt.Println("Total Similarity Score:", answer)
}