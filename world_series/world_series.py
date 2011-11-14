#! /usr/bin/python

def world_series(n, p, q):
	''' P(n1,n2) = Probability of team A wining with games remaining.
		P(0,k) = 1 Team A has won.
		P(k,0) = 0 Team A has lostit will happen.
		P(i,j) =  
	'''
	m = {} # memoization

	for i in range(n):
		m[0,i] = 1
		m[i,0] = 0
		#m[i,i] = 0

	for i in range(1,n): # level by level bottom up approach
		for j in range(1,n):
			m[i,j] = p*m[i-1,j] + q*m[i,j-1]

	for i in range(n):
		for j in range(n):
			print m[i,j],
		print

if __name__ == '__main__':
	p = .25
	q = 1 - p
	world_series(5, p, q)
	world_series(5, q, p)
