package main

import  ( 
	"math" 
	"fmt"
)

type Point struct {
	X int
	Y int
}

//
// argument structure is small: copying it is faster than fiddling with pointers! (redirection costs more than copy)
//
func (self Point) Dist(other Point) float64 {
	arg := (other.X - self.X) * (other.X - self.X) + (other.Y - self.Y) * (other.Y - self.Y)
	return math.Sqrt( float64(arg) )
}

func (self *Point) Add(other Point) {
	self.X += other.X
	self.Y += other.Y
}

// implement the Stringer interface - this way fmt.Println can show the object!
func (self Point) String() string {
	return fmt.Sprintf("x: %d y: %d", self.X, self.Y)
}


func ClearIt(arg *Point) {
	arg.X = 0
	arg.Y = 0
}

func main() {
	p := Point{10, 20}
	other := Point{30, 40}

	fmt.Println("distance between points: ", p.Dist(other))
	p.Add(other)

	fmt.Println("after moving point: ",p)

	ClearIt(&p)
	fmt.Println("after clearIt", p)

}
