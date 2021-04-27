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
g.addLink(9, 10, 84)
g.printGraph()
g.dijkstra(1)

class graphRec:
	def __init__(self, id_node):
		self.id_node = id_node
		self.next = []

	def addLink(self, next_node, weight):
		self.next.append({"node" : next_node, "weight" : weight})

	def printGraph(self):
		print(f"Node : {self.id_node}\nPointe vers :")

		for n in self.next:
			print(n.get("node").id_node)

		for n in self.next:
			n.get("node").printGraph()

	def getNodes(self):
		res = []
		res.append(self.id_node)
		suivants = self.next
		while len(suivants) > 0:
			for node in suivants:
				if not(node["node"].id_node in res):
					res.append(node["node"].id_node)
			new_suivants = []
			for node in suivants:
				new_suivants.extend(node["node"].next)
			suivants = new_suivants
			
		return res

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

	def getNode(self, id_node):
		if (self.id_node == id_node):
			return self

		suivants = self.next
		while len(suivants) > 0:
			for node in suivants:
				if (node["node"].id_node == id_node):
					return node["node"]
			new_suivants = []
			for node in suivants:
				new_suivants.extend(node["node"].next)
			suivants = new_suivants
			
		return None

	def get_neighbours(self, node, visited):

		N = self.getNode(node)

		res = []
		for elem in N.next:
			if not(elem["node"].id_node in visited):
				res.append(elem["node"].id_node)
			
		return res

	def get_distance(self, n1, n2):

		V = self.getNode(n1)
		for elem in V.next:
			if (elem["node"].id_node == n2):
				return elem["weight"]
		return -1

	def dijkstra(self, first_node):
		# init dist
		dist = {}
		nodes = self.getNodes()
		print(f"getNodes : \n{nodes}")
		for node in nodes:
			if node == first_node:
				dist[node] = 0
			else:
				dist[node] = sys.maxsize
		Q = nodes
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



g1 = graphRec(1)
g2 = graphRec(2)
g3 = graphRec(3)
g4 = graphRec(4)
g5 = graphRec(5)
g6 = graphRec(6)
g7 = graphRec(7)
g8 = graphRec(8)
g9 = graphRec(9)
g10 = graphRec(10)

g1.addLink(g2, 85)
g1.addLink(g3, 217)
g1.addLink(g5, 173)
g2.addLink(g6, 80)
g3.addLink(g7, 186)
g3.addLink(g8, 103)
g5.addLink(g10, 502)
g6.addLink(g9, 250)
g8.addLink(g4, 183)
g8.addLink(g10, 167)
g9.addLink(g10, 84)
#g1.printGraph()
g1.dijkstra(1)