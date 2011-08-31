#! /usr/bin/python


def maxsub(a):
	''' This returns the sum of the maximum continuous subsequence. '''
	if len(a) == 1:
		return a[0]
	left  = a[:len(a)/2]
	right = a[len(a)/2:]
	return max(
		max(maxsub(left), sum(left)+lborder(right)),  # Left
		max(maxsub(right), sum(right)+rborder(left)), # Right
		rborder(left) + lborder(right))
	

def lborder(a):
	''' Starting from the left, return the max sum '''
	return max([sum(a[1:x])+a[0] for x in range(len(a))])
	

def rborder(a):
	''' Starting from the right, return the max sum '''
	return  max([sum(a[x:-1])+a[-1] for x in range(len(a))])


if __name__ == '__main__':
	a = [4,-3,5,-2,-1,2,6,2]
	print maxsub(a)

	a = [-4,10,12,-5,-7,8,3,1]
	print maxsub(a)



