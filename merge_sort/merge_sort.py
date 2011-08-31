#! /usr/bin/python

def mergesort(a):
	if len(a) == 1:
		return a

	left  = a[:len(a)/2]
	right = a[len(a)/2:]
	
	left  = mergesort(left)
	right = mergesort(right)
	return merge(left, right)

def merge(left, right):
	''' Takes two sorted lists and merges them, preserving the sorted order '''
	pl = 0 # Index for the left 
	pr = 0 # Index for the right

	a = []

	while (pl < len(left) and pr < len(right)):
		if left[pl] < right[pr]:
			a += [left[pl]]
			pl += 1
		elif left[pl] > right[pr]:
			a += [right[pr]]
			pr += 1
		else:
			a += [left[pl]]
			a += [right[pr]]
			pl += 1
			pr += 1
	
	if pl < len(left) and pr == len(right):
		while pl < len(left):
			a += [left[pl]]
			pl +=1
	elif pr < len(right) and pl == len(left):
		while pr < len(right):	
			a += [right[pr]]
			pr += 1
	
	return a

if __name__ == '__main__':
	a = [4,-3,5,-2,-1,2,6,2]
	print mergesort(a)

	a = [-4,10,12,-5,-7,8,3,1]
	print mergesort(a)



