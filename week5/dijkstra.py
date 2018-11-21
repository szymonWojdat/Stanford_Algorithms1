def get_data(filename):
	data = {}
	with open(filename) as f:
		for line in f:
			line_elements = line.split()
			node = line_elements.pop(0)
			row = {}
			for el in line_elements:
				node_to, length = el.split(sep=',')
				row[int(node_to)] = int(length)
			data[int(node)] = row
	return data


# def dijkstra(graph):
# 	shortest_paths = graph[1]
# 	visited_nodes = []
# 	all_nodes = list(graph.keys())
# 	while not visited_nodes == all_nodes:
# 		shortest_paths_working_copy = shortest_paths.copy()
# 		for v, v_path in shortest_paths.items():
# 			v_neighbors = graph[v]
# 			for w, v_w_path in v_neighbors.items():
# 				if w not in visited_nodes:
# 					current_shortest_to_w = shortest_paths.get(w)
# 					maybe_shortest_to_w = v_path + v_w_path
# 					if not current_shortest_to_w or maybe_shortest_to_w < current_shortest_to_w:
# 						shortest_paths_working_copy[w] = maybe_shortest_to_w
# 					else:
# 						pass
# 		shortest_paths = shortest_paths_working_copy.copy()
# 	return shortest_paths

def dijkstra(graph):
	shortest_paths = {}
	all_nodes = graph.keys()
	for n in all_nodes:
		shortest_paths[n] = 10**6
	shortest_paths[1] = 0  # as we start from 1
	unvisited_nodes = list(all_nodes)
	while len(unvisited_nodes) > 0:
		distances = {}
		# searching for a node with the smallest distance
		for node in shortest_paths.keys():  # = for node in visited nodes:
			for neighbor, distance in graph[node].items():  # searching for the closest node
				if neighbor in unvisited_nodes:
					path = shortest_paths[node] + distance
					distances[path] = neighbor
		min_distance_found = min(distances.keys())
		closest_node = distances[min_distance_found]
		shortest_paths[closest_node] = min_distance_found
		unvisited_nodes.remove(closest_node)
	return shortest_paths


def main():
	graph = get_data('dijkstraData.txt')
	paths = dijkstra(graph)
	paths_to_print = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
	for path in paths_to_print:
		print(path, paths[path])


if __name__ == '__main__':
	main()
