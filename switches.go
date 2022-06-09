package main

import (
	"fmt"
	"time"
)

const n = 1000000

func main() {
	start := time.Now()
	var switches [n]byte

	for person := 1; person <= n; person++ {
		for sw := person - 1; sw < n; sw += person {
			switches[sw] = 1 - switches[sw]
		}
	}

	count := 0
	for _, s := range switches {
		count += int(s)
	}

	end := time.Now()

	fmt.Printf("%d switches on; elapsed time %v\n", count, end.Sub(start))
}
