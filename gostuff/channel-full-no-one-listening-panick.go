package main

// writing a channel to full capacityif no one is listening - panick, deadlock
func main() {

	/*
	ch := make(chan int)
	ch <- 1  // /*fatal error: all goroutines are asleep - deadlock! */
	*/

	ch := make(chan int, 2)
	ch <- 1
	ch <- 2
	
	ch <- 3 
	/*fatal error: all goroutines are asleep - deadlock!

	goroutine 1 [chan send]:
	main.main()
	/home/user/mystuff/my-notes/gostuff/chan1.go:15 +0x56
	*/
}

