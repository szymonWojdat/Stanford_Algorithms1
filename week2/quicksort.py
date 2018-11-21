data = []
comps = 0

with open('QuickSort.txt') as f:
	for line in f:
		data.append(int(line.strip()))


def choose_pivot(arr, n):
	"""
	:param arr: array from which the pivot will be chosen
	:param n: length of arr
	:return: INDEX of the pivot element
	"""
	a = arr[0]
	b = arr[n-1]
	c = arr[(n-1)//2]
	m = [a, b, c]
	m.pop(m.index(max(m)))
	m.pop(m.index(min(m)))
	return arr.index(m[0])


def partition(arr, n, pivot):
	arr[0], arr[pivot] = arr[pivot], arr[0]
	p = arr[0]
	i = 1

	for j in range(1, n):
		if arr[j] < p:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[0], arr[i-1] = arr[i-1], arr[0]
	return arr, i-1


def quicksort(arr):
	n = len(arr)
	if n == 1 or n == 0:
		return arr

	global comps
	comps += n-1

	pivot = choose_pivot(arr, n)

	arr, pivot_after_part = partition(arr, n, pivot)

	left = arr[:pivot_after_part]
	right = arr[pivot_after_part+1:]

	left_sorted = quicksort(left)
	right_sorted = quicksort(right)

	return left_sorted + [arr[pivot_after_part]] + right_sorted


test = [8, 7, 6, 5, 4, 3, 2, 1]
# data = test
data_sorted = quicksort(data)
print(data_sorted)
print(comps)
