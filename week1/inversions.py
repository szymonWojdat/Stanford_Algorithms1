data = []
with open('data.txt', 'r') as f:
	for line in f:
		data.append(int(line.strip()))


def count_split_inversions(a, b):
	# merges two sorted arrays a and b and counts the number of their split inversions
	n_a = len(a)
	n_b = len(b)
	i = 0
	j = 0
	count = 0

	# merging both arrays
	merge_sorted = []
	while i < n_a and j < n_b:
		if a[i] <= b[j]:
			merge_sorted.append(a[i])
			i += 1
		else:
			merge_sorted.append(b[j])
			j += 1
			count += n_a - i

	# copying the remainder
	while i < n_a:
		merge_sorted.append(a[i])
		i += 1
	while j < n_b:
		merge_sorted.append(b[j])
		j += 1

	return merge_sorted, count


def count_inversions(arr):
	# recursion termination condition
	# print(arr)
	if len(arr) == 1:
		return arr, 0

	# dividing the array into half
	mid_point = len(arr)//2
	half1 = arr[:mid_point]
	half2 = arr[mid_point:]

	# logic
	sorted_half1, split_inversions1 = count_inversions(half1)
	sorted_half2, split_inversions2 = count_inversions(half2)
	merged, split_inversions = count_split_inversions(sorted_half1, sorted_half2)
	return merged, split_inversions + split_inversions1 + split_inversions2


# x = [1, 5, 4, 8, 7, 2, 3]
print(count_inversions(data)[1])
