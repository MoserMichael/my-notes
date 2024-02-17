package main

import (
	"fmt"
	"unsafe"
)

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

// It works, now both the Pair instance and Pair reference count as having implement interface IFace
func (pair Pair) Repr() string {
	return fmt.Sprintf("Name: %s Value: %s", pair.Name, pair.Value)
}

func showMe(repr interface{}) {

	// the argument type is a pair of pointers!!!
	// sizeof(interfac{}) 16
	fmt.Printf("sizeof(interfac{}) %d\n", unsafe.Sizeof(repr))

	r, ok := repr.(IFace)
	if ok {
		fmt.Printf("showMe: %s\n", r.Repr())
	}
}

func showMe2(repr IFace) {

	// the argument type is a pair of pointers!!!
	// sizeof(interface-param) 16
	fmt.Printf("sizeof(interface-param) %d\n", unsafe.Sizeof(repr))

	fmt.Printf("showMe2 %s\n", repr.Repr())
}

func main() {

	var pair *Pair
	pair = NewPair("name", "value")

	// sizeof(instance-of-Pair) 32 sizeof(reference-to-Pair) 8
	fmt.Printf("sizeof(instance-of-Pair) %d sizeof(reference-to-Pair) %d\n", unsafe.Sizeof(*pair), unsafe.Sizeof(pair))

	showMe(pair)
	showMe(*pair)

	// a reference to Pair is implementing the interface
	showMe2(pair)

	// an instance of Pair is implementing the interface
	showMe2(*pair)

}
