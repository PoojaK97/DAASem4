def bfs(s):
	global graph
	visited[s]=1
	queue.append(s)
	while queue:
		v=queue.pop(0)
		for i in range(len(graph[v])):
			if visited[graph[v][i]]!=1:
				queue.append(graph[v][i])
				print("---",graph[v][i],end='')
				visited[graph[v][i]]=1

n=int(input("Enter number of nodes in graph:"))
graph=[[]for i in range(n+1)]
visited=[0 for i in range(n+1)]
visited[0]=1
queue=[]
for i in range(1,n+1):
	print("Enter number of nodes connected to node",i)
	ne=int(input())
	print("Enter nodes connected to node",i)
	for j in range(ne):
		val=int(input())
		graph[i].append(val)
print(graph)
s=int(input("Enter source node:"))
print("---BFS TRAVERSAL---")
print(s,end='')
bfs(s)
print()
