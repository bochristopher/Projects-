#course schedule 2 
#topological sort
#not unique
#DFS
#If cycle is detected then we have to return an empty list
#topological sort is not possible
#visiting every node and travel across every single vertex / edge  
#visiting every node and edge at least twice 
#O(V+E) , O(Prerequisites+ courses), courses = vertices 
#use hashset to determine if there is a cycle 

class Solution:
	def findOrder (self, numCourses, int, prerequisites: List[List[int]]) -> List[int]:
		#build adjacency list of prereqs
		prereq = { c :[] for c in range (numCourses) }
		for crs, pre in prerequisites:
			prereq[crs].append(pre)

		# a course has 3 possible states:
		#visited => crs has been added to output 
		#visited => crs has not been added to output, but added to cycle
		#unvisited => crs has not been added to output or cycle 

		output = [] 
		visit, cycle = set(), set()
		def dfs(crs):
			if crs in cycle:
				return False # if course is detected in cycle then return False 
			if crs in visit:
				return True # if course has been visited then it doesnt need to be visited twice 

			cycle.add(crs)#add course to cycle set to make we know next time if we visit it again
			for pre in prereq[c]	
				if dfs(pre) == False #detected cycle
					return False # if returns false then we have to return false as well

			cycle.remove(crs)# remove because it is no longer in the path 
			visit.add(crs)# we can add it to visited because we just went through it and all of its prereqs
			output.append(crs)# we have went through the prereqs and added all them to the output and can add the course to the output 
			#only allowed to add courses after we have added their prerequisites 
			return True #return True because everythin is fine 


		for c in range(numCourses):
			if dfs(c) == False:
				return [] # have to return empty list because it return False because of the cycle

		return output 
