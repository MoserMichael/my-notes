package main

import "fmt"

// List represents a singly-linked list that holds
// values of any type.
type List[T any] struct {
	next *List[T]
	val  T
}

func  (self *List[T]) Add(cadd *List[T]) {

	(*cadd).next = self.next
	self.next = cadd
}

func  (self *List[T]) Count() int {

	ret := 0
	for self != nil {
		ret += 1
		self = self.next
	}
	return ret
}

func main() {
 link := &List[int]{}
 after := &List[int]{}

 link.Add(after)

 fmt.Println("Number of links:", link.Count())

}

