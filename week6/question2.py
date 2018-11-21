from question1 import load_data


class Heap:
	def __init__(self, is_min=True):
		self.data = []
		self.size = 0
		self.is_min = is_min

	def _compare(self, parent, child):
		parent_val = self.data[parent]
		child_val = self.data[child]
		return self.is_min == (parent_val < child_val) or parent_val == child_val

	@staticmethod
	def _get_parent(index):
		if index == 0:
			return None
		else:
			return (index + 1) // 2 - 1

	def _get_children(self, index):
		index += 1
		index_child_1 = 2 * index - 1
		index_child_2 = index_child_1 + 1

		if index_child_1 > self.size - 1:
			index_child_1 = None

		if index_child_2 > self.size - 1:
			index_child_2 = None

		return index_child_1, index_child_2

	def _swap(self, index1, index2):
		self.data[index1], self.data[index2] = self.data[index2], self.data[index1]

	def insert(self, element):
		self.data.append(element)
		self.size += 1
		index = self.size - 1
		parent = self._get_parent(index)
		while parent is not None and not self._compare(parent, index):
			self._swap(index, parent)
			index = parent  # self._get_parent(index)
			parent = self._get_parent(index)

	def extract_top(self):
		def pick_child_to_swap(left, right):
			nonlocal self
			if left is None:  # right child will always be None in this case
				cts = None
			elif right is None or self._compare(left, right):
				cts = left
			else:  # right child wins
				cts = right
			return cts
		self._swap(0, self.size-1)
		top = self.data.pop(-1)
		self.size -= 1
		index = 0
		left_child, right_child = self._get_children(0)
		child_to_swap = pick_child_to_swap(left_child, right_child)
		while child_to_swap is not None and not self._compare(index, child_to_swap):
			self._swap(index, child_to_swap)
			index = child_to_swap
			left_child, right_child = self._get_children(index)
			child_to_swap = pick_child_to_swap(left_child, right_child)
		return top


def main():
	data = load_data('Median.txt')
	min_heap = Heap(is_min=True)
	max_heap = Heap(is_min=False)

	first = data.pop(0)
	max_heap.insert(first)
	sum_of_medians = first  # initialization

	for number in data:
		median = max_heap.data[0]
		if max_heap.size == min_heap.size:
			if number >= median:
				min_heap.insert(number)
				element = min_heap.extract_top()
				max_heap.insert(element)
			else:
				max_heap.insert(number)
		elif max_heap.size == min_heap.size + 1:
			if number >= median:
				min_heap.insert(number)
			else:
				max_heap.insert(number)
				element = max_heap.extract_top()
				min_heap.insert(element)
		else:
			print('ERROR: something went wrong')
			break
		current_median = max_heap.data[0]
		sum_of_medians += current_median  # breakpoint w 5685, bo przy dodawaniu kolejnej liczby jest blad max_heap.data
		sum_of_medians = sum_of_medians % 10000
	print(sum_of_medians)


if __name__ == '__main__':
	main()
