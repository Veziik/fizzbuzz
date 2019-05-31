#! /usr/bin/env python3
import sys

if len(sys.argv) > 2:
 print('specify number to end at')
 exit(1)

limit = int(sys.argv[1])
i = 0

while i <= limit:
	out = ''
	if( i % 3 == 0 ):
		out += 'fizz'
	
	if( i % 5 == 0 ):
		out += 'buzz'

	if len(out) == 0:
		out += str(i) 

	print(out)
	i+=1