#Number of islands - leetcode 200 
class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		if not grid: #input validation 
			return 0

		rows, cols = len(grid), len(grid[0]) # get number of rows and number of cols
		visit = set() # mark islands using set, easier, 
		islands = 0  # count number of islands 

		def bfs(r,c):
			#breadth first search is not a recursive algo
			# it is iterative so we need a data structure to use for memory
			#q is normally used 
			q = collections.deque()
			visit.add(r,c)#mark position as visited 
			q.append((r,c))#add to queue

			while q:#while not empty 
				row, col = q, popleft()# used because of bfs
				#use pop for dfs, means popright 
				#popleft pops the first instead of the last like popright
				directions = [[1,0], [-1,0], [0,1], [0,-1]]
				for dr, dc in directions:
					r,c = row + dr, col + dc
					if (r in range(rows) and 
						c in range(cols) and 
						grid[r][c] == "1" and 
						(r,c) not in visit):
						q.append((r,c))
						visit.add((r,c))#using add bc of set 

		for r in range (rows): # iterate through all rows and cols
			for c in range(cols):
				if grid[r][c] == "1" and (r,c) not in visit:
					#if visit then we have to traverse and mark it 
					#also check if visited 
					bfs(r,c)	
					islands += 1 #increment island 
		return islands 