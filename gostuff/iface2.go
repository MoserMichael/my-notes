package main

import "fmt"

type IFace interface {
	Repr() string
}
type Pair struct {
	Name  string
	Value string
}

func NewPair(name string, value string) *Pair {
	return &Pair{Name: name, Value: value}
}

/* It works, but only the Pair reference counts has having implemented interface IFace */
func (pair *Pair) Repr() string {
	return fmt.Sprintf("Name: %s Value: %s", pair.Name, pair.Value)
}

func showMe(repr interface{}) {

	r, ok := repr.(IFace)
	if ok {
		fmt.Printf("showMe: %s\n", r.Repr())
	}
}

func showMe2(repr IFace) {
	fmt.Printf("showMe2 %s\n", repr.Repr())
}

func main() {
	pair := NewPair("name", "value")

	showMe(pair)

	// you can pass the instance as any type, but the instance does not implement the interface!
	showMe(*pair)

	showMe2(pair)

	// this does not compile - only the reference to Pair is implementing the interface
	//showMe2(*pair)

}
