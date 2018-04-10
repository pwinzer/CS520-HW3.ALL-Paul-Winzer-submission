
import pprint

# global vars
G = {}
visited = []
visit_order = []
pp = pprint.PrettyPrinter(indent=2)


def algoIterDeep(filename='ex.txt', v=0, q=7): 
	'''
	does a depth limited, depth first search on the graph
	represented by the adjacency matrix in <filename> param

	starting at the root <v>

	returns when the node <q> is found
	if not found, returns null after full traversal
	
	'''
	# only need to declare this because we wipe it out
	global visited

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
	
	i = 0
	done = None
	while done is None and len([x for x in visited if x == 0]):
		# clear visited records so we don't immediately skip
		visited = [0 for x in visited]
		done = DLDFS(v, q, i)
		print 'Result? {}'.format(done)
		print 'Visited list for the iteration:'
		pp.pprint(visited)
		i += 1
		print

	print '\nOrder nodes were visited/discovered for the first time:'
	pp.pprint(visit_order)


def DLDFS(v, q, d=0):
	visited[v] = 1

	print 'Visiting {}'.format(v)

	if v not in visit_order:
		visit_order.append(v)
		print '...for the first time'

	if v == q:
		return v
	
	if d > 0:
		for w in G[v]:
			if (visited[w] == 0):
				hit = DLDFS(w, q, d-1)
				if hit is not None:
					return hit

	return None 


