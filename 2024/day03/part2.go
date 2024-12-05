package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	var matches []string
	do := true
	sum := 0

	data, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	input := string(data)

	regex := regexp.MustCompile(`mul\(\d+,\d+\)|do\(\)|don't\(\)`)
	matches = append(matches, regex.FindAllString(input, -1)...)

	for _, match := range matches {
		if match == "do()" {
			do = true
		} else if match == "don't()" {
			do = false
		} else {
			regex := regexp.MustCompile(`\d+`)
			nums := regex.FindAllString(match, 2)
			if do {
				x, err := strconv.Atoi(nums[0])
				if err != nil {
					fmt.Println("Error converting x:", err)
					continue
				}
				y, err := strconv.Atoi(nums[1])
				if err != nil {
					fmt.Println("Error converting y:", err)
					continue
				}
				sum += x * y
			}
		}
	}
	fmt.Println(sum)
}
