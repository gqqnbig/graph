import random

import networkx as nx
import pytest

import Program


def test_swapTwice():
	m1 = [[1, 2, 3],
		  [4, 5, 6],
		  [7, 8, 9]]
	m2 = Program.swap(m1, 0, 1)
	assert m1 != m2

	m3 = Program.swap(m2, 0, 1)
	assert m1 == m3


def canonicalizeTest1():
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
	Program.showGraph(m, False)

	m2 = Program.canonicalize(m, 2)
	Program.prettyPrint(m2, ['ro', 'N'] + [str(i) for i in range(7)])

	Program.showGraph(m2, False)


def canonicalizeTest2():
	m = [  # root	p	2
		[None, 'a', 'b'],  # root
		[None, None, None],  # p
		[None, None, None],  # 2
	]
	Program.showGraph(m, False)

	m2 = Program.canonicalize(m, 2)
	Program.prettyPrint(m2)

	Program.showGraph(m2, False)


def canonicalizeTest3():
	m = [  # root	p	1	2
		[None, None, 'a', 'b'],  # root
		[None, None, None, None],  # p
		['e', 'c', None, 'f'],  # 1
		[None, 'd', None, None],  # 2
	]
	Program.showGraph(m, False)

	m2 = Program.canonicalize(m, 2)
	Program.prettyPrint(m2)

	Program.showGraph(m2, False)


def assignEdgeLabel(m, p):
	"""

	:param m:
	:param p: probability of assigning a duplicate edge label.
	:return:
	"""
	size = len(m)
	c = 0
	rand = random.Random()
	for i in range(size):
		for j in range(size):
			if m[i][j] == 1:
				if c > 0 and rand.random() <= p:
					k = rand.randrange(c)
					m[i][j] = chr(ord('a') + k)
				else:
					m[i][j] = chr(ord('a') + c)
					c += 1
			else:
				m[i][j] = None


def test_duplicateEdgeLabels():
	labeledNodeCount = 2
	m1 = [
		[None, None, 'c', None, 'c', None, None, None],
		['a', None, None, None, None, None, None, None],
		[None, 'e', None, None, None, None, None, None],
		[None, None, 'f', None, None, None, None, None],
		['d', None, None, None, None, None, None, None],
		[None, None, None, None, 'e', None, None, None],
		['f', None, None, None, None, None, None, None],
		['a', None, None, None, None, None, None, None]]

	m2 = m1.copy()
	#
	m2 = Program.swap(m2, 3, 2)
	m2 = Program.swap(m2, 2, 5)
	m2 = Program.swap(m2, 3, 7)
	m2 = Program.swap(m2, 4, 2)
	m2 = Program.swap(m2, 5, 2)
	#
	# Program.prettyPrint(m2)
	# Program.canonicalize(m2, labeledNodeCount)
	# print('----------------')
	# Program.prettyPrint(m2)

	# size = len(m2)
	# for c in range(5):
	# 	i = random.randrange(labeledNodeCount, size)
	# 	j = random.randrange(labeledNodeCount, size)
	# 	print(f'swap {i}, {j}')
	# 	m2 = Program.swap(m2, i, j)

	assert Program.getHash(Program.canonicalize(m1, labeledNodeCount)) == Program.getHash(Program.canonicalize(m2, labeledNodeCount)), 'm2 is \n' + Program.pretty(m2)


def test_duplicateEdgeLabels2():
	labeledNodeCount = 2
	m1 = [
		[None, None, 'c', None, 'c', None, None, None],
		['a', None, None, None, None, None, None, None],
		[None, 'e', None, None, None, None, None, None],
		[None, None, 'f', None, None, None, None, None],
		['d', None, None, None, None, None, None, None],
		[None, None, None, None, 'e', None, None, None],
		['f', None, None, None, None, None, None, None],
		['a', None, None, None, None, None, None, None]]

	m2 = m1.copy()
	m2 = Program.swap(m2, 6, 7)
	m2 = Program.swap(m2, 2, 4)
	m2 = Program.swap(m2, 2, 6)
	m2 = Program.swap(m2, 4, 7)
	m2 = Program.swap(m2, 3, 7)
	#
	# Program.prettyPrint(m2)
	# Program.canonicalize(m2, labeledNodeCount)
	# print('----------------')
	# Program.prettyPrint(m2)

	# size = len(m2)
	# for c in range(5):
	# 	i = random.randrange(labeledNodeCount, size)
	# 	j = random.randrange(labeledNodeCount, size)
	# 	print(f'swap {i}, {j}')
	# 	m2 = Program.swap(m2, i, j)

	assert Program.getHash(Program.canonicalize(m1, labeledNodeCount)) == Program.getHash(Program.canonicalize(m2, labeledNodeCount)), 'm2 is \n' + Program.pretty(m2)


def test_duplicateEdgeLabelsRandom():
	labeledNodeCount = 2
	m1 = [
		[None, None, 'c', None, 'c', None, None, None],
		['a', None, None, None, None, None, None, None],
		[None, 'e', None, None, None, None, None, None],
		[None, None, 'f', None, None, None, None, None],
		['d', None, None, None, None, None, None, None],
		[None, None, None, None, 'e', None, None, None],
		['f', None, None, None, None, None, None, None],
		['a', None, None, None, None, None, None, None]]

	m2 = m1.copy()

	size = len(m2)
	for c in range(5):
		i = random.randrange(labeledNodeCount, size)
		j = random.randrange(labeledNodeCount, size)
		print(f'swap {i}, {j}')
		m2 = Program.swap(m2, i, j)

	assert Program.getHash(Program.canonicalize(m1, labeledNodeCount)) == Program.getHash(Program.canonicalize(m2, labeledNodeCount)), 'm2 is \n' + Program.pretty(m2)


def test_canonicalizeHashRandom():
	labeledNodeCount = 2
	G = nx.generators.scale_free_graph(8, delta_out=0.1)
	A = nx.adjacency_matrix(G)
	m = A.toarray().tolist()
	assignEdgeLabel(m, 0.3)

	# Program.showGraph(m, False)

	m1 = m.copy()
	size = len(m)
	for c in range(5):
		i = random.randrange(labeledNodeCount, size)
		j = random.randrange(labeledNodeCount, size)
		m1 = Program.swap(m1, i, j)

	# m2 = Program.canonicalize(m, 2)
	print('m')
	Program.prettyPrint(m)

	print('m1')
	Program.prettyPrint(m1)

	# Program.showGraph(m2, False)

	assert Program.getHash(Program.canonicalize(m, labeledNodeCount)) == Program.getHash(Program.canonicalize(m1, labeledNodeCount))


def test_canonicalizeHash():
	m1 = [
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
	m2 = [  # root	X	1	2	3	4	5	6	7
		[None, None, None, None, None, None, 'i', None, None],  # root
		[None, None, None, None, None, None, None, None, None],  # X
		[None, None, None, None, None, None, None, None, None],  # 1
		[None, None, None, None, None, None, None, None, 'g'],  # 2
		[None, 'a', None, None, None, None, None, None, 'd'],  # 3
		['e', None, None, None, 'b', None, None, None, None],  # 4
		[None, None, None, None, None, None, None, 'f', None],  # 5
		[None, None, None, None, None, 'c', None, None, None],  # 6
		['h', None, 'j', None, None, None, None, None, None],  # 7
	]

	hash1 = Program.getHash(Program.canonicalize(m1, 2))
	hash2 = Program.getHash(Program.canonicalize(m2, 2))

	assert hash1 == hash2, 'Isomorphic graphs should return the same hash.'


@pytest.mark.skip
def test_canonicalizeHash1():
	m1 = [
		['a', 'b', None, None, None, None, None, None],
		[None, None, 'c', None, None, None, None, None],
		['d', None, None, None, None, None, None, None],
		['e', None, None, None, None, None, None, 'f'],
		['g', None, None, None, None, None, 'h', None],
		[None, None, None, None, None, None, None, 'i'],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
	]

	Program.showGraph(m1, False, title='m1', layout=nx.planar_layout)

	m2 = Program.canonicalize(m1, 2)
	Program.showGraph(m2, False, title='m2', layout=nx.planar_layout)


def test_noOutgoingEdges():
	m1 = [
		[None, 'a', None, None, None, None, None, None],
		['b', None, 'c', None, None, None, None, 'd'],
		[None, None, None, None, None, None, None, None],
		['e', None, None, None, None, None, None, None],
		['f', None, None, None, None, None, 'g', None],
		['h', None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
	]

	m2 = [
		[None, 'a', None, None, None, None, None, None],
		['b', None, None, None, None, 'd', 'c', None],
		[None, None, None, None, None, None, None, None],
		['h', None, None, None, None, None, None, None],
		['f', None, 'g', None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		['e', None, None, None, None, None, None, None],
	]
	assert Program.getHash(Program.canonicalize(m1, 2)) == Program.getHash(Program.canonicalize(m2, 2))


if __name__ == '__main__':
	test_canonicalizeHash1()
