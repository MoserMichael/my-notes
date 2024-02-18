package main

import (
	"fmt"
	"strings"
)

func main() {

	// golang doesn'thave a char class - for unicode characters it's 'rune'.
	var slc []rune

	for i := 0; i < 10; i++ {
		// you can append something to an empty null slice!!!
		slc = append(slc, rune('b'))
	}
	fmt.Println(string(slc))

	var sb strings.Builder

	for i := 0; i < 1000; i++ {
		// method WriteString of strings.Builder can cope with null receiver !!!
		sb.WriteString("a")
	}
	fmt.Println(sb.String())

}
