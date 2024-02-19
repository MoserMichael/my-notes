package main

import (
	"fmt"
	"math"
)

type Circle struct {
	r float64
}

func (c *Circle) area() float64 {
	if c == nil {
    // initalize nil receiver
	// (only for this method)	
		c = new(Circle)
		c.r = 10
	}
	return math.Pi * c.r * c.r
}

func main() {
	var c *Circle
	fmt.Println(c.area()) // returns area

	// will throw panic for c.r, after calling c.area() the object has still nil fields.
	//fmt.Println(c.r)
}
