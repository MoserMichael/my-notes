package main

import (
	"fmt"
	"strings"
)

func main() {

	// golang doesn'thave a char class - for unicode characters it's 'rune'.
	var slc []rune

	for i := 0; i < 10; i++ {
		// you can append something to an empty slice value !!!
		slc = append(slc, rune('b'))
	}
	fmt.Println(string(slc))

	// the values of the fields  for struct strings.Builder are all nil
	// see: https://github.com/golang/go/blob/master/src/strings/builder.go
	// 
	var sb strings.Builder

	for i := 0; i < 1000; i++ {
		// method WriteString of strings.Builder can cope with uninitialized fields in its struct.
		// they check if the buffer is nill and init it.
		sb.WriteString("a")
	}
	fmt.Println(sb.String())

}
