memo = []

with open('kargerMinCut.txt') as f:
	for line in f:
		numbers = line.split()
		numbers.pop(0)
		numbers = [int(el)-1 for el in numbers]
		memo.append(numbers)
		print(numbers, ',')

with open('data_ready.py', 'w') as f:
	f.write(memo)
