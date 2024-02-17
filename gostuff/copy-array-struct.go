package main

import "fmt"

type strA struct {
	names []string
}

type strB struct {
	names []string
}

func main() {
	a := &strA{}
	b := &strB{names: a.names}

	a.names = append(a.names, "kuku")

	fmt.Printf("a.names: %s\n", a.names)
	fmt.Printf("b.names: %s\n", b.names)
}
