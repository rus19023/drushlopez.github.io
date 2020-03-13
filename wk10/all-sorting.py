import random
import time
import copy
size1 = 100
size2 = 10000
size3 = 1000000
span = 1000000
threshold = 20

#---------------------------------------
# Insertion Sort
#---------------------------------------
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
				
#---------------------------------------
# Selection Sort
#---------------------------------------			
def selection_sort(A):
	for i in range (0, len(A) - 1):
		minIndex = i
		for j in range (i+1, len(A)):
			if A[j] < A[minIndex]:
				minIndex = j
		if minIndex != i:
			A[i], A[minIndex] = A[minIndex], A[i]

#---------------------------------------
# Bubble Sort
#---------------------------------------
# not optimized			
def bubble_sort1(A):
	for i in range (0, len(A) - 1):
		for j in range (0, len(A) - i - 1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
				
# optimized to exit if no swaps occur		
def bubble_sort2(A):
	for i in range (0, len(A) - 1):
		done = True
		for j in range (0, len(A) - i - 1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
				done = False
		if done:
			return

#---------------------------------------
# Merge Sort
#---------------------------------------				
def merge_sort(A):
	merge_sort2(A, 0, len(A)-1)
	
def merge_sort2(A, first, last):
	if last-first < threshold and first < last:
		quick_selection(A, first, last)
	elif first < last:
		middle = (first + last)//2
		merge_sort2(A, first, middle)
		merge_sort2(A, middle+1, last)
		merge(A, first, middle, last)
		
def merge(A, first, middle, last):
	L = A[first:middle]
	R = A[middle:last+1]
	L.append(999999999)
	R.append(999999999)
	i = j = 0
	
	for k in range (first, last+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
#---------------------------------------
# Quick Sort
#---------------------------------------
def quick_sort(A):
	quick_sort2(A, 0, len(A)-1)
	
def quick_sort2(A, low, hi):
	if hi-low < threshold and low < hi:
		quick_selection(A, low, hi)
	elif low < hi:
		p = partition(A, low, hi)
		quick_sort2(A, low, p - 1)
		quick_sort2(A, p + 1, hi)
	
def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	s = sorted([A[low], A[mid], A[hi]])
	if s[1] == A[low]:
		return low
	elif s[1] == A[mid]:
		return mid
	return hi
	
def partition(A, low, hi):
	pivotIndex = get_pivot(A, low, hi)
	pivotValue = A[pivotIndex]
	A[pivotIndex], A[low] = A[low], A[pivotIndex]
	border = low

	for i in range(low, hi+1):
		if A[i] < pivotValue:
			border += 1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low]

	return (border)
	
def quick_selection(x, first, last):
	for i in range (first, last):
		minIndex = i
		for j in range (i+1, last+1):
			if x[j] < x[minIndex]:
				minIndex = j
		if minIndex != i:
			x[i], x[minIndex] = x[minIndex], x[i]
	
#--------------RANDOM ORDER----------------------
#------------------------------------------------
# size = 100
#------------------------------------------------
print("\nRandom Order\n---------------------------------")
w = [random.randint(0, span) for a in range(0, size1)]
t1 = time.clock()
insertion_sort3(w)
print("Insertion Sort(size=", str(size1),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, span) for a in range(0, size1)]
t1 = time.clock()
selection_sort(w)
print("Selection Sort(size=", str(size1),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, span) for a in range(0, size1)]
t1 = time.clock()
bubble_sort2(w)
print("Bubble Sort(size=", str(size1),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, span) for a in range(0, size1)]
t1 = time.clock()
merge_sort(w)
print("Merge Sort(size=", str(size1),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, span) for a in range(0, size1)]
t1 = time.clock()
quick_sort(w)
print("Quick Sort(size=", str(size1),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, span) for a in range(0, size1)]
t1 = time.clock()
w.sort()
print("Tim Sort(size=", str(size1),"): ", (time.clock()-t1) * 1000)
#------------------------------------------------
# size = 10,000
#------------------------------------------------
w = [random.randint(0, span) for a in range(0, size2)]
t1 = time.clock()
insertion_sort3(w)
print("Insertion Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, span) for a in range(0, size2)]
t1 = time.clock()
selection_sort(w)
print("Selection Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, span) for a in range(0, size2)]
t1 = time.clock()
bubble_sort2(w)
print("Bubble Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, span) for a in range(0, size2)]
t1 = time.clock()
merge_sort(w)
print("Merge Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, span) for a in range(0, size2)]
t1 = time.clock()
quick_sort(w)
print("Quick Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, span) for a in range(0, size2)]
t1 = time.clock()
w.sort()
print("Tim Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)
#------------------------------------------------
# size = 1,000,000
#------------------------------------------------
w = [random.randint(0, span) for a in range(0, size3)]
t1 = time.clock()
merge_sort(w)
print("Merge Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, span) for a in range(0, size3)]
t1 = time.clock()
quick_sort(w)
print("Quick Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, span) for a in range(0, size3)]
t1 = time.clock()
w.sort()
print("Tim Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)

# ----------------ALREADY SORTED-----------------
#------------------------------------------------
# size = 10,000
#------------------------------------------------
print("\nAlready Sorted\n---------------------------------")

w = [a for a in range(0, size2)]
t1 = time.clock()
insertion_sort3(w)
print("Insertion Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

t1 = time.clock()
selection_sort(w)
print("Selection Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

t1 = time.clock()
bubble_sort2(w)
print("Bubble Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

t1 = time.clock()
merge_sort(w)
print("Merge Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

t1 = time.clock()
quick_sort(w)
print("Quick Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

t1 = time.clock()
w.sort()
print("Tim Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)
#------------------------------------------------
# size = 1,000,000
#------------------------------------------------
w = [a for a in range(0, size3)]
t1 = time.clock()
merge_sort(w)
print("Merge Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)

t1 = time.clock()
quick_sort(w)
print("Quick Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)

t1 = time.clock()
w.sort()
print("Tim Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)

# ----------------REVERSE SORTED-----------------
#------------------------------------------------
# size = 10,000
#------------------------------------------------
print("\nReverse Sorted\n---------------------------------")

w = [a for a in range(0, size2)]
w.reverse()
t1 = time.clock()
insertion_sort3(w)
print("Insertion Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [a for a in range(0, size2)]
w.reverse()
t1 = time.clock()
selection_sort(w)
print("Selection Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [a for a in range(0, size2)]
w.reverse()
t1 = time.clock()
bubble_sort2(w)
print("Bubble Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [a for a in range(0, size2)]
w.reverse()
t1 = time.clock()
merge_sort(w)
print("Merge Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [a for a in range(0, size2)]
w.reverse()
t1 = time.clock()
quick_sort(w)
print("Quick Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [a for a in range(0, size2)]
w.reverse()
t1 = time.clock()
w.sort()
print("Tim Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)
#------------------------------------------------
# size = 1,000,000
#------------------------------------------------
w = [a for a in range(0, size3)]
w.reverse()
t1 = time.clock()
merge_sort(w)
print("Merge Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)

w = [a for a in range(0, size3)]
w.reverse()
t1 = time.clock()
quick_sort(w)
print("Quick Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)

w = [a for a in range(0, size3)]
w.reverse()
t1 = time.clock()
w.sort()
print("Tim Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)

#--------------RANDOM ORDER, MANY DUPLICATES------------------
#------------------------------------------------
# size = 10,000
#------------------------------------------------
print("\nRandom Order, Many Duplicates\n---------------------------------")

w = [random.randint(0, size2//10) for a in range(0, size2)]
t1 = time.clock()
insertion_sort3(w)
print("Insertion Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, size2//10) for a in range(0, size2)]
t1 = time.clock()
selection_sort(w)
print("Selection Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0,size2//10) for a in range(0, size2)]
t1 = time.clock()
bubble_sort2(w)
print("Bubble Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, size2//10) for a in range(0, size2)]
t1 = time.clock()
merge_sort(w)
print("Merge Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, size2//10) for a in range(0, size2)]
t1 = time.clock()
quick_sort(w)
print("Quick Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, size2//10) for a in range(0, size2)]
t1 = time.clock()
w.sort()
print("Tim Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)
#------------------------------------------------
# size = 1,000,000
#------------------------------------------------
w = [random.randint(0, size2//10) for a in range(0, size3)]
t1 = time.clock()
merge_sort(w)
print("Merge Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, size2//10) for a in range(0, size3)]
t1 = time.clock()
#quick_sort(w)
#print("Quick Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)

w = [random.randint(0, size2//10) for a in range(0, size3)]
t1 = time.clock()
w.sort()
print("Tim Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)4