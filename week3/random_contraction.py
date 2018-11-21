from data_ready import adjList
from random import choice

NUM_REPS = 212000

# adjList = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]


def merge(arr_orig, n1, n2):
	# arr = arr_orig.copy()
	arr = []
	for row in arr_orig:
		tmp = row.copy()
		arr.append(tmp)
	while n2 in arr[n1]:
		arr[n1].remove(n2)
	while n1 in arr[n2]:
		arr[n2].remove(n1)
	arr[n1].extend(arr[n2])
	arr[n2] = []
	for node in arr:
		while n2 in node:
			node.remove(n2)
			node.append(n1)
	return arr


def size_of_adjlist(arr):
	return len(arr) - arr.count([])


def count_contractions(arr):
	while [] in arr:
		arr.remove([])
	if len(arr[0]) == len(arr[1]):
		return len(arr[0])
	else:
		print('ERROR')
		return -1


def rand_contraction(arr):
	rand_range = list(range(len(arr)))
	# while size_of_adjlist(arr) > 2:
	while len(rand_range) > 2:
		node2 = choice(rand_range)
		rand_range.remove(node2)
		node1 = choice(rand_range)
		arr = merge(arr, node1, node2)
	return count_contractions(arr)


minimum = 1000
for _ in range(NUM_REPS):
	rc = rand_contraction(adjList)
	print(rc)
	if rc < minimum:
		minimum = rc

print('\nBest result: {}'.format(minimum))
