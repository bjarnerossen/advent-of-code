package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
)

// SPLIT EACH LINE -- SAVE IN ARRAY
func parseInput(input string) []string {
	// memory := strings.Split(strings.TrimSpace(input), "\n")
	// return memory
}

// USE REGEX IN ORDER TO FIND COORDINATES THROUGH PATTERN
func findInstructions(memories) {
	// Compile the regex pattern for valid mul instructions
	// regex := regexp.MustCompile(`mul$begin:math:text$(\\d+),(\\d+)$end:math:text$`)

	// // Find all matches in the input
	// matches := regex.FindAllStringSubmatch(input, -1)
	// for _, match := range matches {
	// 	fmt.Printf("Instruction: %s, X: %s, Y: %s\n", match[0], match[1], match[2])
	// }
}

// EXTRACT AND PARSE NUMBERS --> GET SUM
func parseNumbersAndGetSum(matches) {
	sum := 0
	for _, match := range matches {
		// match[1] and match[2] contain the numbers
		x, _ := strconv.Atoi(match[1])
		y, _ := strconv.Atoi(match[2])
		sum += x * y
	}
	return sum
}

func main() {
	// Read input dynamically
	data, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	input := string(data)

	memories := parseInput(input)                                                // PARSE INPUT
	matches := findInstructions(memories)                                        // FIND AND RETURN MATCHING INSTRUCTIONS
	fmt.Println("Sum of valid multiplications:", parseNumbersAndGetSum(matches)) // PARSE MATCHES FROM REGEX AND GET RESULT
}