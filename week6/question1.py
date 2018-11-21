def load_data(filename):
	arr = []
	with open(filename) as f:
		for line in f:
			arr.append(int(line))
	return arr


def two_sum(arr, twosum):
	hashmap = dict()
	for el in arr:
		hashmap[el] = True
	distinct_arr = hashmap.keys()
	for el in distinct_arr:
		if hashmap.get(twosum - el):
			return True
	return False


def main():
	arr = load_data('algo1-programming_prob-2sum.txt')
	total = 0
	for t in range(-10000, 10001):
		if t % 10 == 0:
			print(t)
		total += two_sum(arr, t)
	print('\ntotal: {}'.format(total))


if __name__ == '__main__':
	main()
