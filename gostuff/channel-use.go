package main

import (
	"log"
	"os"
)

func main() {
	logger := log.New(os.Stderr, "", 0)

	ch := make(chan int)

	// the next line panics: no one is listening on the channel:
	// ch <- 1

	// when someone is listening you can push two items to the channel (the docs say that the channel capacity is one, not clear)

	f := func() {
		var num int

		for num != -1 {
			num = <-ch
			logger.Println("got", num)
		}
		logger.Println("func exit")
	}

	go f()

	for n := 1; n < 10; n++ {
		logger.Println("push:", n)
		ch <- n
	}
	logger.Println("push-last:", -1)
	ch <- -1

}
