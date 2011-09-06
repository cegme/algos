#! /usr/bin/python

"""
	Add two matrix together
"""

def add(a,b):
	return map(lambda x: add_row(x[0],x[1]), zip(a,b))

def add_row(a,b):
	return map(sum, zip(a,b))

def sub_row(a,b):
	return map(lambda x: x[0]-x[1], zip(a, b))

if __name__ == '__main__':
	m1 = [[1,2,3],[4,5,6],[7,8,9]]
	m2 = [[9,8,7],[6,5,4],[3,2,1]]
	print add(m1,m2)
