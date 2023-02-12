def travesese_graph (some_graph, start_node)
	to_visit = [start_node] @#ist with one line 
	visited = [] # empty I have not visited anythin

	while to_visit:
			node_to_checkout = to_visit.pop(0)
			for neighbor_node not in some_graph [node_to_checkout]::
					if neighbor_node not in visited:
							to_visit.insert(0, neighbor_node)
							visited.append(neighbor_node)

	return visited

	traveses_graph(graph_dict, 'B')
	set(graph_dict.keys())
	set(traverse_graph(graph_dict,'B'))
	