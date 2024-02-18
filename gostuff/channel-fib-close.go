package main

import (
	"log"
	"os"
)

func makeFib(ch chan int64) {
	logger := log.New(os.Stderr, "", 0)

	n_1 := int64(1)
	n_2 := int64(1)

	for idx := 1; idx < 20; idx += 1 {

		logger.Println("ch <- :: post: ", idx, n_1)
		ch <- n_1

		num := n_1 + n_2
		n_1 = n_2
		n_2 = num
	}
	logger.Println("<- closing channel")
	close(ch)
}

func main() {
	logger := log.New(os.Stderr, "", 0)

	capacity := 2
	logger.Print("Channel capacity: ", capacity)
	ch := make(chan int64, capacity)

	go makeFib(ch)

	for {
		res, ok := <-ch
		if !ok {
			logger.Println("channel closed")
			break
		}
		logger.Println("<-ch :: received: ", res)
	}

}
