#!/usr/bin/env python 

def func(x):
	print 'x is ', x
	x=2
	print 'Changed local x', x

x= 50
func(x)
print 'x is still',x