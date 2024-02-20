package main

import "fmt"

type Point struct {
	x int
	y int
}

func main() {

	// allocate a structure and set the structure fields
	ptr := &Point{x: 10, y:20}

	fmt.Printf("&Point{} %v %T\n", ptr, ptr)

	ptrb := new(Point)

	fmt.Printf("&Point{} %v %T\n", ptrb, ptrb)


}
