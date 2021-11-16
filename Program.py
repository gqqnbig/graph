import matplotlib.pyplot as plt
import networkx as nx
import scipy as sp
import scipy.sparse  # call as sp.sparse
import numpy as np


# As of April 2021, matplotlib draws unlabeled curved edges or labeled straight edges.
# https://stackoverflow.com/a/67238706/746461


def getEdgeLabel(m):
	edge_labels = {}
	size = len(m)
	for i in range(size):
		for j in range(size):
			if m[j][i] != 0:
				edge_labels[(i, j)] = m[j][i]

	return edge_labels


def showGraph(m, printUnlabeledNodes: bool):
	size = len(m)
	vertexes = {}
	vertexes = {0: 'root', 1: 'X'}
	if printUnlabeledNodes:
		vertexes.update({i: i for i in range(2, size)})
	# print(f'There are {size} nodes in the graph. The first node is root, the second is X, the remaining is {vertexes}.')

	edge_labels = getEdgeLabel(m)

	m = (np.array(m) != '0') + 0

	# m = numpy.array(m)
	G = nx.from_numpy_matrix(m, create_using=nx.DiGraph)
	pos = nx.spring_layout(G, seed=3113794651)  # positions for all nodes

	# G2.add_nodes_from(vertexes)
	# nx.draw(G, pos)
	nx.draw_networkx_nodes(G, pos)
	nx.draw_networkx_labels(G, pos, vertexes, font_size=22, font_color="red")
	nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=20)
	nx.draw_networkx_edge_labels(G, pos, edge_labels, bbox=dict(alpha=0))
	plt.axis('equal')
	plt.show()



def swap(m, i, j):
	"""
	Swap row i and j of the matrix as well as column i and column j.

	:param m:
	:param i:
	:param j:
	:return:
	"""
	isNp = m is np.ndarray
	if isNp is False:
		m = np.array(m)

	m[[i, j], :] = m[[j, i], :]
	m[:, [i, j]] = m[:, [j, i]]

	if isNp is False:
		return m.tolist()
	else:
		return m


if __name__ == '__main__':
	# m[i][j] means i has an edge to j.
	m = [
		[0, 0, 0, 0, 0, 0, 'i', 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 'a', 0, 'd', 0, 0, 0, 0, 0],
		['h', 0, 0, 0, 0, 'j', 0, 0, 0],
		[0, 0, 0, 'g', 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 'f', 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 'c'],
		['e', 0, 'b', 0, 0, 0, 0, 0, 0],
	]

	# m2 = swap(m, 0, 1)
	showGraph(m, True)
