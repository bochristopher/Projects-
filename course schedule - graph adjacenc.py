#course schedule - graph adjacency 
#
#uses data structure called adjacency list
#O(n+p)
#courses cannot be completed if there is a cycle detected 

class Solution:
def canFinish(self, numCourses:int, prerequisits: List[List[int]]) -> bool:
	#map each course to prereq list
	preMap = { i : [] for i in range(numCourses)}
	for crs, pre in prerequisits:
		preMap[crs].append(pre)

	#visitSet = all courses along the curr DFS path
	visitSet = set()
	def dfs(crs):# pass in current course 
		if crs in visitSet:
			return False #detected loop
		if preMap[crs] == []:
			return True #has no prequistes 

		visitSet.add(crs)# add to visit set
		for pre in preMap[crs]:# loop through prereqs
			if not dfs(pre):return False # each one run dfs
			#if one course returns false 
			#return false for the entire function
		visitSet.remove(crs)#remove course after visiting 
		preMap[crs] =[]#set to empty list in case have to run again
		#prevents having to run dfs on all of its neighbors
		return True

	for crs in range(numCourses):#search through every course of all the courses that we have
		if not dfs(crs): return False#if any of them return false then we return false 
	return True #if they dont return false then we return false

