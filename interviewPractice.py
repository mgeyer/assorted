from copy import deepcopy
from Queue import PriorityQueue
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


