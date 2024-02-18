package main

import (
	"log"
	"os"
)

func main() {
	logger := log.New(os.Stderr, "", 0)

	// with capacity two - can push two items, without panic!
	ch := make(chan int, 2)

	logger.Printf("push one")
	ch <- 1

	logger.Printf("push two")
	ch <- 1

	// but the third one panics
	//logger.Printf("push three")
	//ch <- 3

}
