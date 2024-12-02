package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	var answer int
	var left []int
	var right []int

	input, err := os.ReadFile("input.txt") // Read input file
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

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
	sort.Ints(left)
	sort.Ints(right)

	if len(left) != len(right) {
		fmt.Println("Slices are not of equal length")
		return
	}

	for i := 0; i < len(left); i++ {
		diff := right[i] - left[i]
		answer += diff
	}
	fmt.Println(answer)
}