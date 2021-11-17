import hashlib

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


# As of April 2021, matplotlib draws unlabeled curved edges or labeled straight edges.
# https://stackoverflow.com/a/67238706/746461


def getEdgeLabel(m):
	edge_labels = {}
	size = len(m)
	for i in range(size):
		for j in range(size):
			if m[i][j]:
				edge_labels[(i, j)] = m[i][j]

	return edge_labels


def showGraph(m, printUnlabeledNodes: bool, seed=None, title=None, layout=None):
	size = len(m)
	vertexes = {}
	vertexes = {0: 'root', 1: 'X'}
	if printUnlabeledNodes:
		vertexes.update({i: i for i in range(2, size)})
	# print(f'There are {size} nodes in the graph. The first node is root, the second is X, the remaining is {vertexes}.')

	edge_labels = getEdgeLabel(m)

	m = (np.array(m) != None) + 0

	# m = numpy.array(m)
	G = nx.from_numpy_matrix(m, create_using=nx.DiGraph)
	if layout is None:
		pos = nx.spring_layout(G, seed=seed)  # positions for all nodes
	else:
		pos = layout(G)

	# G2.add_nodes_from(vertexes)
	# nx.draw(G, pos)
	nx.draw_networkx_nodes(G, pos)
	nx.draw_networkx_labels(G, pos, vertexes, font_size=22, font_color="red")
	nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=20)
	nx.draw_networkx_edge_labels(G, pos, edge_labels, bbox=dict(alpha=0), font_size=15)
	if title:
		plt.title(title)
	plt.axis('equal')
	plt.show()
	# plt.savefig(title + '.png')
	# plt.close('all')


def swap(m, i, j):
	"""
	Swap row i and j of the matrix as well as column i and column j.

	:param m:
	:param i:
	:param j:
	:return:
	"""
	if i == j:
		return m

	isNp = m is np.ndarray
	if isNp is False:
		m = np.array(m)
	else:
		m = m.copy()

	m[[i, j], :] = m[[j, i], :]
	m[:, [i, j]] = m[:, [j, i]]

	if isNp is False:
		return m.tolist()
	else:
		return m


def _sortKeys(row, m, startIndex):
	for i in range(startIndex, len(row)):
		for j in range(i + 1, len(row)):
			if row[i] is None and row[j] is None:
				continue
			elif row[i] is None and row[j] is not None:
				m = swap(m, i, j)
				t = row[i]
				row[i] = row[j]
				row[j] = t
			elif row[i] is not None and row[j] is None:
				continue
			elif row[i] > row[j]:
				m = swap(m, i, j)
				t = row[i]
				row[i] = row[j]
				row[j] = t

	return m


def _findSmallestRow(m, startIndex):
	"""

	:param m:
	:param startIndex:
	:return: the index of the smallest row
	"""
	# size = len(m)
	rows = m[startIndex:]
	rows = [''.join([e if e else '~' for e in r]) for r in rows]
	return startIndex + rows.index(min(rows))


def _sort(m, labeledNodeCount, iteration):
	# m[i][j] means i has an edge to j.
	size = len(m)
	if iteration >= size:
		return m

	if iteration >= labeledNodeCount:
		i = _findSmallestRow(m, iteration)
		m = swap(m, i, iteration)

	row = m[iteration]

	if labeledNodeCount + iteration < size:
		m = _sortKeys(row, m, labeledNodeCount + iteration)
	return m


def canonicalize(m, labeledNodeCount):
	"""
	m[i][j] means i has an edge to j.

	:param m:
	:param labeledNodeCount:
	:return:
	"""
	size = len(m)
	if size <= labeledNodeCount:
		return m

	for i in range(size):
		m = _sort(m, labeledNodeCount, i)
	return m


def prettyPrint(m, nodeNames=None, nonePlaceholder='-'):
	if nodeNames:
		print('\t' + '\t'.join(nodeNames))

	rows = ['\t'.join([str(cell) if cell is not None else nonePlaceholder for cell in row]) for row in m]

	if nodeNames:
		for i in range(len(rows)):
			rows[i] = nodeNames[i] + '\t' + rows[i]

	print('\n'.join(rows))


def getHash(m):
	s = [''.join([str(cell) if cell is not None else '-' for cell in row]) for row in m]
	s = ''.join(s)

	sha = hashlib.sha1(s.encode('utf-8'))
	return sha.hexdigest()


if __name__ == '__main__':
	# m[i][j] means i has an edge to j.
	m = [
		[None, None, None, None, None, None, 'i', None, None],
		[None, None, None, None, None, None, None, None, None],
		[None, 'a', None, 'd', None, None, None, None, None],
		['h', None, None, None, None, 'j', None, None, None],
		[None, None, None, 'g', None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, 'f', None],
		[None, None, None, None, None, None, None, None, 'c'],
		['e', None, 'b', None, None, None, None, None, None],
	]
	showGraph(m, False)

	# m2 = swap(m, 0, 1)
	# m2 = _sort(m, 2, 2)
	m2 = canonicalize(m, 2)
	prettyPrint(m2)

	showGraph(m2, False)
