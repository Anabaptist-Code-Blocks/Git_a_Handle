#!/usr/bin/env python
#
#  count.py
#  
#
#  Created by Andy Balholm on 12/16/08.
#  Copyright (c) 2008 Northland Graphics. All rights reserved.
#

from time import clock

def count1(x):
	i = 1
	while i <= x:
		i += 1
		
def count2(x):
	for i in range(x):
		pass
count = count1

goal = 2000000

start = clock()

count(goal)

stop = clock()

print("It took", stop - start, "seconds to count to", goal)

