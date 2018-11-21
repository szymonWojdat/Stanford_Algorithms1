import sys

sys.setrecursionlimit(875714)


def get_data(filename):
	data = []
	with open(filename) as f:
		for line in f:
			line_elements = line.split()
			data.append([int(el) for el in line_elements])
	return data


def dfs(graph, node_from, explored=set(), finish_time=[], component_size=1):
	explored.add(node_from)  # mark node as explored
	edges_from_node = list(filter(lambda x: x[0] == node_from, graph))  # edges coming out of 'node'
	for edge in edges_from_node:
		node_to = edge[1]
		if node_to not in explored:
			component_size += 1
			explored, finish_time, component_size = dfs(graph, node_to, explored, finish_time, component_size)
	finish_time.append(node_from)
	return explored, finish_time, component_size


def dfs_loop(graph, nodes=[]):
	explored = set()
	finish_time = []
	sizes = []

	# instead of changing node numbers
	if len(nodes) == 0:
		nodes = sorted(list(set([row[0] for row in graph])))
	nodes = list(reversed(nodes))

	for node in nodes:
		if node not in explored:
			explored, finish_time, component_size = dfs(graph, node, explored, finish_time)
			sizes.append(component_size)

	return sizes, finish_time


def reverse_edges(graph):
	rev_graph = []
	for edge in graph:
		rev_graph.append([edge[1], edge[0]])
	return rev_graph


# TODO - optimize memory mgmt
def main():
	g = get_data('SCC.txt')
	# g = get_data('test')
	r = reverse_edges(g)

	_, finish_times = dfs_loop(r)
	print('\n\n\n')
	sizes, _ = dfs_loop(g, finish_times)
	top_scores = list(reversed(sorted(sizes)))[:10]
	print(top_scores)


if __name__ == '__main__':
	main()
