import sys
'''
Spécification

Sorte : graph

Opérations :
	graph : _ -> graph

'''

class graphList:
	def __init__(self):
		self.nodes = []
		self.links = []

	def addNode(self, id_node):
		self.nodes.append(id_node)

	def addLink(self, source, target, weight):
		self.links.append({"source" : source, "target" : target, "weight" : weight})

	def printGraph(self):
		print(f"nodes : {self.nodes}\nlinks : {self.links}")

	def removeMin(self, Q, dist):
		min_dist = sys.maxsize
		min_rank = 0
		for i in range(len(Q)):
			if dist[Q[i]] < min_dist:
				min_dist = dist[Q[i]]
				min_rank = i
		res = Q[min_rank]
		del Q[min_rank]
		return res

	def get_neighbours(self, node, visited):
		res = []
		for link in self.links:
			source = link.get("source")
			target = link.get("target")
			if (source == node) and (target not in visited):
				res.append(target)
			elif (target == node) and (source not in visited):
				res.append(source)
		return res

	def get_distance(self, n1, n2):
		for link in self.links:
			source = link.get("source")
			target = link.get("target")
			if (source == n1 and target == n2) or (source == n2 and target == n1):
				return link.get("weight")
		return -1

	def dijkstra(self, first_node):
		# init dist
		dist = {}
		for node in self.nodes:
			if node == first_node:
				dist[node] = 0
			else:
				dist[node] = sys.maxsize
		Q = self.nodes
		S = []

		while len(Q) > 0:
			v = self.removeMin(Q, dist)
			S.append(v)

			neighbours = self.get_neighbours(v, S)

			for neighbour in neighbours:
				d = dist[v] + self.get_distance(v, neighbour)
				if d < dist[neighbour]:
					dist[neighbour] = d

		print(f"dist: {dist}")

g = graphList()
g.addNode(1)
g.addNode(2)
g.addNode(3)
g.addNode(4)
g.addNode(5)
g.addNode(6)
g.addNode(7)
g.addNode(8)
g.addNode(9)
g.addNode(10)
g.addLink(1, 2, 85)
g.addLink(1, 3, 217)
g.addLink(1, 5, 173)
g.addLink(2, 6, 80)
g.addLink(3, 7, 186)
g.addLink(3, 8, 103)
g.addLink(5, 10, 502)
g.addLink(6, 9, 250)
g.addLink(8, 4, 183)
g.addLink(8, 10, 167)
g.printGraph()
g.dijkstra(1)

class graphRec:
	def __init__(self, id_node):
		self.id_node = id_node
		self.visited = False
		self.next = []

	def addLink(self, next_node, weight):
		self.next.append({"node" : next_node, "weight" : weight})

	def printGraph(self):
		print(f"Node : {self.id_node}\nPointe vers :")

		for n in self.next:
			print(n.get("node").id_node)

		for n in self.next:
			n.get("node").printGraph()



g1 = graphRec(1)
g2 = graphRec(2)
g3 = graphRec(3)
g4 = graphRec(4)
g5 = graphRec(5)

g1.addLink(g2, 12)
g1.addLink(g3, 25)
g2.addLink(g4, 8)
g4.addLink(g5, 33)
g3.addLink(g5, 5)
g1.printGraph()