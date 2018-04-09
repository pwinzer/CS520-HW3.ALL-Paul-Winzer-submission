import pprint

G = {}
visited = []
visit_order = []
pp = pprint.PrettyPrinter(indent=2)

def algoDFS(filename='ex.txt', v=0): #TODO remove default filename

	# read the doc and close the doc
	with open(filename) as f:
		doc = f.readlines()
	f.close()

	i = 0
	for line in doc:
		# init node's entry in visited
		visited.append(0)
		# init node's entry in adj list
		G[i] = []
		# clean her up
		l = line.strip().split(',')
		
		# create adj list entry for the node
		for j in range(0, len(l)):
			if l[j] == '1' and j != i: # don't want node in it's own adj list entry
				G[i].append(j)

		i+=1

	print '\nAdjancency list:'
	pp.pprint(G)
	
	DFS(v)

	print '\nVisited list:'
	pp.pprint(visited)

	print '\nOrder nodes were visited:'
	pp.pprint(visit_order)

def DFS(v):
	visited[v] = 1
	visit_order.append(v)
	for w in G[v]:
		if (visited[w] == 0):
			DFS(w)

