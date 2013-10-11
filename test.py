from Queue import PriorityQueue

items = [1,2,3,4,5,6,7,8]

print items[:len(items)/2]
print items[len(items)/2:]

print items

x = PriorityQueue()

print x

def factorial(n):
	if n <=1:
		return 1
	else:
		return n * factorial(n-1)

def factorial_iterative(n):
	total = 1
	for i in range(n+1):
		if i != 0:
			total *= i

	return total

print factorial(7)

print factorial_iterative(8)


def remove_duplicates(list):
	seen = []
	final = []
	for item in list:
		if item not in seen:
			seen.append(item)
			final.append(item)
	return final

def reverse_list(list):
	so_far = []
	for item in list:
		so_far = [item] + so_far
	return so_far

print remove_duplicates([1, 1, 2, 3, 1, 4, 5, 3, 2])
print [1, 1, 2, 3, 1, 4, 5, 3, 2]
print reverse_list([1, 1, 2, 3, 1, 4, 5, 3, 2])