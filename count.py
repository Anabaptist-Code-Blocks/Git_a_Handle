#!/usr/bin/env python
#
#  count.py
#  
#
#  Created by Andy Balholm on 12/16/08.
#  Copyright (c) 2008 Northland Graphics. All rights reserved.
#

from time import perf_counter

def count1(x):
	i = 1
	while i <= x:
		i += 1
		
def count2(x):
	for i in range(x):
		pass
count = count1

goal = 2000000

start = perf_counter()

count(goal)

stop = perf_counter()

print("It took", stop - start, "seconds to count to", goal)

