package main

import (
	"log"
	"os"
)

func makeFib(ch chan int64) {
	logger := log.New(os.Stderr, "", 0)

	n_1 := int64(0)
	n_2 := int64(1)

	idx := 0

	for idx < 20 {
		logger.Println("ch <- :: post: ", idx, n_1)
		ch <- n_1

		num := n_1 + n_2
		n_1 = n_2
		n_2 = num
		idx += 1
	}
	ch <- -1

}

/*
output with capacity == 0 (default)

Channel capacity: 0
ch <- :: post:  0 0
ch <- :: post:  1 1
<-ch :: received:  0
<-ch :: received:  1
ch <- :: post:  2 1
ch <- :: post:  3 2
<-ch :: received:  1
<-ch :: received:  2
ch <- :: post:  4 3
ch <- :: post:  5 5
<-ch :: received:  3
<-ch :: received:  5
ch <- :: post:  6 8
ch <- :: post:  7 13
<-ch :: received:  8
<-ch :: received:  13
ch <- :: post:  8 21
ch <- :: post:  9 34
<-ch :: received:  21
<-ch :: received:  34
ch <- :: post:  10 55
ch <- :: post:  11 89
<-ch :: received:  55
<-ch :: received:  89
ch <- :: post:  12 144
ch <- :: post:  13 233
<-ch :: received:  144
<-ch :: received:  233
ch <- :: post:  14 377
ch <- :: post:  15 610
<-ch :: received:  377
<-ch :: received:  610
ch <- :: post:  16 987
ch <- :: post:  17 1597
<-ch :: received:  987
<-ch :: received:  1597
ch <- :: post:  18 2584
ch <- :: post:  19 4181
<-ch :: received:  2584
<-ch :: received:  4181
<-ch :: received:  -1

output with capacity == 2 

Channel capacity: 2
ch <- :: post:  0 0
ch <- :: post:  1 1
ch <- :: post:  2 1
ch <- :: post:  3 2
<-ch :: received:  0
<-ch :: received:  1
<-ch :: received:  1
<-ch :: received:  2
ch <- :: post:  4 3
ch <- :: post:  5 5
ch <- :: post:  6 8
ch <- :: post:  7 13
<-ch :: received:  3
<-ch :: received:  5
<-ch :: received:  8
<-ch :: received:  13
ch <- :: post:  8 21
ch <- :: post:  9 34
ch <- :: post:  10 55
ch <- :: post:  11 89
<-ch :: received:  21
<-ch :: received:  34
<-ch :: received:  55
<-ch :: received:  89
ch <- :: post:  12 144
ch <- :: post:  13 233
ch <- :: post:  14 377
ch <- :: post:  15 610
<-ch :: received:  144
<-ch :: received:  233
<-ch :: received:  377
<-ch :: received:  610
ch <- :: post:  16 987
ch <- :: post:  17 1597
ch <- :: post:  18 2584
ch <- :: post:  19 4181
<-ch :: received:  987
<-ch :: received:  1597
<-ch :: received:  2584
<-ch :: received:  4181
<-ch :: received:  -1
*/
func main() {
	logger := log.New(os.Stderr, "", 0)

	capacity := 0
	logger.Print("Channel capacity: ", capacity)
	ch := make(chan int64, capacity)

	go makeFib(ch)

	var res int64
	for res != -1 {
		res = <-ch
		logger.Println("<-ch :: received: ", res)
	}

}
