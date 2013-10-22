from copy import deepcopy
from Queue import PriorityQueue
from Queue import Queue
'''
Sorting Algorithms
'''
def quicksort(items):
	items = deepcopy(items)
	# Base Case
	if len(items) <= 1:
		return items
	#pick the pivot AND remove it so that you always reduce the size of the array
	pivot = items[len(items) / 2]
	items.remove(pivot)
	#create two lists less | great
	lesser = []
	greater = []
	#for each x put into less or great
	for item in items:
		if item <= pivot:
			lesser.append(item)
		else:
			greater.append(item)
	# return the items less on the left + the pivot + the sorted greater values
	return quicksort(lesser) + [pivot] + quicksort(greater)

def bubblesort(items):
	items = deepcopy(items)
	#while list not sorted (can tell if no replacement)
	change = True
	while change:
		# for each item if greater than next replace both
		noChange = False
		for i in range(len(items) - 1):
			if items[i] > items[i+1]:
				noChange = True
				temp = items[i+1]
				items[i+1] = items[i]
				items[i] = temp
		change = noChange
	return items

def mergesort(items):
	items = deepcopy(items)
	# Base Case
	if len(items) <= 1:
		return items
	#We split the array into two halfs
	left = items[:len(items)/2]
	right = items[len(items)/2:]

	#sort each side
	left = mergesort(left)
	right = mergesort(right)

	#Merge the two sides
	return merge(left, right)

def merge(left, right):
	result = []
	while len(left) > 0 or len(right) > 0:
		if len(left) > 0 and len(right) > 0:
			if left[0] <= right[0]:
				result.append(left[0])
				left.remove(left[0])
			else:
				result.append(right[0])
				right.remove(right[0])
		elif len(left) > 0:
			result += left
			left = []
		else:
			result += right
			right = []
	return result

def heapsort(items):
	items = items[:]

list1 = [1, 4, 5, 7, 2, 1, 8, 9, 0]

print quicksort(list1)
print list1
print bubblesort(list1)
print list1
print mergesort(list1)


'''
Searching Algorithms
'''

def linearSearch(val, items):
	for item in items:
		if val == item:
			return True

	return False

# Array must be sorted already
def binarySearch(val, items):
	if len(items) <= 1:
		if len(items) == 0 or val != items[0]:
			return False
		else:
			return True
	pivot = len(items) / 2
	if val == items[pivot]:
		return True
	elif val <= items[pivot]:
		return binarySearch(val, items[:pivot])
	else:
		return binarySearch(val, items[pivot:])

orderedList = mergesort(list1)

print "Success" if linearSearch(2, orderedList) else "Nope"
print "Success" if linearSearch(99, orderedList) else "Nope"

print "Success" if binarySearch(0, orderedList) else "Nope"
print "Success" if binarySearch(99, orderedList) else "Nope"

#graphs

#djikstra's shortest path

def djikstra(start, end, graph):
	# Initiate dictionaries for distance to each vertex
	distances = {}
	# Predecessors so we can return a path not just distance
	predecessors = {}

	visited = []

	to_visit = pQueue()

	to_visit.put(start, 0)

	while not to_visit.empty():
		v = to_visit.get(True)
		v_distance = v[1]
		v_name = v[0]
		print v_name

		visited.append(v_name)
		distances[v] = v_distance
		if v_name == end:
			print "get here"
			break

		for neighbor in graph[v_name]:
			if neighbor not in visited:
				dist_to_neighbor = graph[v_name][neighbor] + v_distance
				if not to_visit.contains(neighbor) or to_visit.returnVal(neighbor) > dist_to_neighbor:
					to_visit.put(neighbor, dist_to_neighbor)
					predecessors[neighbor] = v_name

	return (distances, predecessors)


#takes only positive values
class pQueue:
	queue = {}

	def put(self, item, val):
		self.queue[item] = val

	def get(self, reverse=False):
		if reverse:
			val = 10000000
		else:
			val = -1000000
		item_to_return = None
		for key, value in self.queue.iteritems():
			if reverse:
				if value < val:
					val = value
					item_to_return = key
			else:
				if value > val:
					val = value
					item_to_return = key
		self.queue.pop(item_to_return)
		return (item_to_return, val)

	def empty(self):
		return not self.queue

	def contains(self, item):
		return item in self.queue

	def returnVal(self, item):
		if item in self.queue:
			return self.queue[item]

G1 = {'s': {'u': 5}, 'u': {'v': 3}, 'v':{}}


G = {'s':{'u':10, 'x':5}, 'u':{'v':1, 'x':2}, 'v':{'y':4}, 'x':{'u':3, 'v':9, 'y':2}, 'y':{'s':7, 'v':6}}

print djikstra('s', 'v', G)

def findDuplicates(arr):
	seen = []
	duplicates = []
	for item in arr:
		if item in seen and item not in duplicates:
			duplicates.append(item)
		if item not in seen:
			seen.append(item)
	return duplicates

def factorial(num):
	fact = 1
	if num == 0:
		return fact
	while num > 0:
		fact *= num
		num -= 1
	return fact

def removeFromString(toRemove, str):
	for character in toRemove:
		str = str.replace(character, '')
	return str

print findDuplicates([1, 1, 2, 3, 4, 1, 2, 6, 7, 8])

print factorial(3)

print removeFromString('aeiou', 'Markus Geyer')


def removeEverySecond(arr):
	second = False
	newArr = []
	for item in arr:
		if not second:
			newArr.append(item)
		second = not second
		print second
	return newArr

def mergeSort2(arr):
	arr = deepcopy(arr)
	if len(arr) <= 1:
		return arr
	else:
		half = len(arr) / 2
		return merge2(mergeSort2(arr[:half]), mergeSort2(arr[half:]))

def merge2(arr1, arr2):
	retArr = []
	while len(arr1) > 0 and len(arr2) > 0:
		left = arr1[0]
		right = arr2[0]
		if left <= right:
			retArr.append(left)
			arr1.remove(left)
		else:
			retArr.append(right)
			arr2.remove(right)
	retArr = retArr + arr1 + arr2
	return retArr




print removeEverySecond([1, 2, 3, 4, 5, 6, 7, 8])

print mergeSort2([1, 3, 4, 2, 1, 8, 9, 10, 2, 3])

#Node has val, children (ordered left to right)
def depthfirst(node, toFind):
	toCheck = [node]
	while toCheck:
		currentNode = toCheck.pop()
		if currentNode.value == toFind:
			return True
		else:
			toCheck.append(children.reverse())
	return False

def breadthfirst(node, toFind):
	toCheck = Queue()
	toCheck.put(node)
	while not toCheck.empty():
		currentNode = toCheck.get()
		if currentNode.value == toFind:
			return True
		else:
			for child in currentNode.children:
				toCheck.put(child)
	return False

def largestIncreasingSubsequence(arr):
	largestSoFar = []
	currentSequence = []
	lastItem = None
	for num in arr:
		if num >= lastItem:
			currentSequence.append(num)
		else:
			if len(currentSequence) > len(largestSoFar):
				largestSoFar = currentSequence
			currentSequence = [num]
		lastItem = num
	if len(currentSequence) > len(largestSoFar):
		largestSoFar = currentSequence
	return largestSoFar

print largestIncreasingSubsequence([1,2,3,4,-1, -2, 3, 4, 5, 6, 7])

#return all sets of primes such that p * q <= n
def multPrimes(n):
	p = 1
	q = 2
	sets = []
	if n < 2:
		return None
	while p*q <= n:
		sets.append((p, q))
		p = q
		q += 1
		while not isPrime(q):
			q += 1
	return sets

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def primesBefore(n):
	primes = []
	for i in range(n):
		if isPrime(i):
			primes.append(i)
	return primes

print multPrimes(10000)

print primesBefore(1000)

def isPermutation(a, b):
	for character in a:
		if character in b:
			b = stringRemoveFirst(character, b)
		else:
		    return False
	if not b:
		return True
	return False

def stringRemoveFirst(letter, string):
	str1 = ''
	letterRemoved = False
	for character in string:
		if letter == character and not letterRemoved:
			letterRemoved = True
		else:
			str1 += character
	return str1


print isPermutation('cat', 'tac')

print isPermutation('cat', 'catch')


def returnDuplicates(arr):
	seensofar = []
	duplicates = []
	for num in arr:
		if num in seensofar:
			duplicates.append(num)
		else:
			seensofar.append(num)
	return duplicates

print returnDuplicates([1, 2, 3, 4, 1, 2, 4, 6])

def mergesort3(arr):
	if len(arr) == 1:
		return arr
	return merge3(mergesort3(arr[:len(arr)/2]), mergesort3(arr[len(arr)/2:]))

def merge3(a, b):
	merged = []
	while a and b:
		if a[0] <= b[0]:
			merged.append(a[0])
			a.remove(a[0])
		else:
			merged.append(b[0])
			b.remove(b[0])
	return merged + a + b

print mergesort3([1, 2, 3, 4, 2, 3, 7, 4, 5,6,8])

def leapfrog(arr, startIndex, endIndex):
	indexesSeen = []
	currentIndex = startIndex
	while True:
		nextIndex = currentIndex + arr[currentIndex]
		if nextIndex > len(arr) or nextIndex < 0:
			return False
		elif nextIndex == endIndex:
			return True
		elif nextIndex in indexesSeen:
			return False
		else:
			indexesSeen.append(currentIndex)
			currentIndex = nextIndex

print leapfrog([1, 2, -1, 3], 0, 3)

print leapfrog([1, 2, -1, 3], 2, 3)

print leapfrog([1, 2, -1, 3], 3, 3)

def findLargerThan(bst, val):
	currentNode = bst.root
	while True:
		if currentNode.value > val:
			return currentNode.value
		else:
			if currentNode.right:
				currentNode = currentNode.right
			else:
				return False
 
def reverseArray(arr):
	for i in range(len(arr) / 2):
		temp = arr[i]
		arr[i] = arr[len(arr) - (i + 1)]
		arr[len(arr) - (i + 1)] = temp
	return arr

def reverseArrayNonDestructive(arr):
	toReturn = []
	for item in arr:
		toReturn = [item] + toReturn
	return toReturn

print reverseArray([1, 2, 3, 4, 5])

print reverseArrayNonDestructive([1, 2, 3, 4])

class Stack:
	mins = []
	stack = []

	def getMin(self):
		return self.mins[-1]

	def push(self, item):
		self.stack.append(item)
		if len(self.mins) == 0 or item <= self.mins[-1]:
			self.mins.append(item)

	def pop(self):
		val = self.stack.pop()
		if val == self.mins[-1]:
			self.mins.pop()
		return val

testStack = Stack()

testStack.push(2)
testStack.push(3)
testStack.push(1)

print testStack.mins
print testStack.stack
print testStack.getMin()
print testStack.pop()
print testStack.getMin()

# Selects a pivot, splits all values below and above that value
# recursively does the same on both halves
def quickSort(arr):
	if len(arr) <= 1:
		return arr
	pivot = len(arr) / 2
	pivotValue = arr[pivot]
	left = []
	right = []
	for i in range(len(arr)):
		if i != pivot:
			if arr[i] <= pivotValue:
				left.append(arr[i])
			else:
				right.append(arr[i])
	return quickSort(left) + [pivotValue] + quickSort(right)

print quickSort([1, 5, 4, 2, 3, 7, 8, 4, 2, 1])

def bubbleSort2(arr):
	noChange = False
	while not noChange:
		noChange = True
		for i in range(len(arr)-1):
			if arr[i] > arr[i+1]:
				temp = arr[i+1]
				arr[i+1] = arr[i]
				arr[i] = temp
				noChange = False
	return arr

print bubbleSort2([1, 5, 4, 2, 3, 7, 8, 4, 2, 1])

def findMax(arr):
	max = None
	for item in arr:
		if item > max:
			max = item
	return max



