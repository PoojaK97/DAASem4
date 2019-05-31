def dfs(s):
	global graph
	visited[s]=1
	for i in range(len(graph[s])):
		if visited[graph[s][i]]!=1:
			print("-|-",graph[s][i],end='')
			dfs(graph[s][i])

n=int(input("Enter number of nodes:"))
graph=[[] for i in range(n)]
visited=[0 for i in range(n)]
for i in range(n):
	print("Enter number of nodes connected to",i)
	ne=int(input())
	print("Enter nodes connected to node",i)
	for j in range(ne):
		val=int(input())
		graph[i].append(val)
s=int(input("Enter source node:"))
print("---DFS Traversal---")
print(s,end='')
dfs(s)
print()
