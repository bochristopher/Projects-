#graph traversal 

def validTree(self, m, edges):
	if not n:
		return True


	adj = { i:[] for i in range(n) }# i is the number of nodes
	#creating pair in the hashmap 
	#each pair is going to be a value of the node and an empty list
	for n1, n2 in edges:#edge is a pair of nodes connected
		adj[n1].append(n2)#adjacency list
		adj[n2].append(n1)

	visit = set()#set that tracks all nodes visited 
	def dfs(i, prev):# i is the value of node we are visiting
		#prev is the previous node visited
		if i in visit: # if i has been visited 
			return False

		visit.add(i)#if it hasnt then add it to visited 
		for j in adj[i]:
			if j == prev:
				continue # skip iteration of the loop
			if not dfs(j,i):# if this does not  
				return False # detected a loop
		return True # did not detect a loop

	return dfs(0, -1) and n ==len(visit)
	#return values
	#pass value from the first to the last (0,-1) # -1 is the last value 
	#returns true is both statements return true above
	#if every node has been visited = n # that means the graph is a tree
	#if there has was not a cycle detected then first statement equals true
	