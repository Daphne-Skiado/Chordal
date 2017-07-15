

def lexBFS(net):
#Input: The class of a network
#Output: An ordering of the vertices (sigma)
	sigma = []                           
	label = []
	id_search = []
	for i in range(net.pop):
		sigma.append(-1)
		label.append('')
	for i in range(net.pop-1,-1,-1):
		u = pick_unnum(id_search,label)
		sigma[i] = u
		for j in net.nodes[u].neighbors:
			if j.id not in sigma:
				if j.id not in id_search:
					id_search.append(j.id)
				label[j.id] = label[j.id] + str(i)
		id_search.remove(u)
	print(sigma)
	return sigma

def is_triangulated(net):
#Check if graph is triangulated
	sigma = lexBFS(net)
	for i in range(len(sigma)):
		neighbors = net.nodes[sigma[i]].neighbors
		for j in range(i):
			if net.nodes[sigma[j]] in neighbors:
				neighbors.remove(net.nodes[sigma[j]])
		if not clique(neighbors):
			return False
	return True


def pick_unnum(id_search,label):
#In every loop of lexBFS returns the vertex with the largest label which is unnumbered
	id_max = -1
	maximum = ''
	if(len(id_search) == 0):
		id_search.append(0)
		return 0
	for i in range(0,len(id_search)):
		if label[id_search[i]] > maximum:
			id_max = id_search[i]
			maximum = label[id_search[i]]
	return id_max

def clique(v):
#Checks if the vertices in the list v form a clique
	for i in v:
		for j in v:
			if i != j and i not in j.neighbors:
				 return False
	return True


	
