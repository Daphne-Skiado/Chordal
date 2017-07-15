import random
from node import node

class triangulated:
#Class that creates a random triangulated network
	def __init__(self,n):
		self.pop = n
		self.nodes = []


		if self.pop % 2 == 0 :
			#If population is even creation begins with two connected nodes
			node1 = node(len(self.nodes))
			self.nodes.append(node1)
			node2 = node(len(self.nodes))
			self.nodes.append(node2)
			node2.neighbors.append(node1)
			node1.neighbors.append(node2)
		else :
			#If population is odd creation begins with one node
			node1 = node(len(self.nodes))
			self.nodes.append(node1)
		while len(self.nodes) < self.pop:
			#In every loop the algorithm adds two new nodes that form a triangul with a randomly chosen node
			peak = self.nodes[random.randint(0,len(self.nodes)-1)]
			self.trig(peak)
			print('len(self.nodes) = ',len(self.nodes))


	def trig(self,peak):
		node2 = node(len(self.nodes))
		self.nodes.append(node2)
		node3 = node(len(self.nodes))
		self.nodes.append(node3)
		peak.neighbors.append(node2)
		peak.neighbors.append(node3)
		node2.neighbors.append(node3)
		node2.neighbors.append(peak)
		node3.neighbors.append(node2)
		node3.neighbors.append(peak)





