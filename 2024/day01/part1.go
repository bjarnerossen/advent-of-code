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
		parts := strings.Split(line, "   ")
		fmt.Println(parts[0])
		}
	}