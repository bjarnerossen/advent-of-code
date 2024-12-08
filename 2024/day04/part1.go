package main

import (
	"fmt"
	"os"
	"strings"
)

func countXMAS(grid []string) int {
	word := "XMAS"

	// The dimensions of the grid
	rows := len(grid)
	cols := len(grid[0])

	// Directions: right, down, left, up, diagonals
	directions := [][2]int{
		{0, 1},   // right
		{1, 0},   // down
		{0, -1},  // left
		{-1, 0},  // up
		{1, 1},   // down-right diagonal
		{1, -1},  // down-left diagonal
		{-1, 1},  // up-right diagonal
		{-1, -1}, // up-left diagonal
	}
	count := 0

	// Check every position in the grid
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			// For each direction, check if we can form the word "XMAS"
			for _, dir := range directions {
				if canFormWord(grid, r, c, dir[0], dir[1], word) {
					count++
				}
			}
		}
	}
	return count
}

// Helper function to check if the word can be formed starting from (r, c) in a given direction
func canFormWord(grid []string, r, c, dr, dc int, word string) bool {
	for i := 0; i < len(word); i++ {
		// Calculate the new position
		newR := r + i*dr
		newC := c + i*dc
		// Check if the new position is out of bounds or doesn't match the word
		if newR < 0 || newR >= len(grid) || newC < 0 || newC >= len(grid[0]) || grid[newR][newC] != word[i] {
			return false
		}
	}
	return true
}

func main() {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// Split the input into lines
	grid := strings.Split(strings.TrimSpace(string(data)), "\n")

	result := countXMAS(grid)
	fmt.Println(result)
}
