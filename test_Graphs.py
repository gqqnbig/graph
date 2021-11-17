import networkx as nx

import pytest

import Program


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


def assignEdgeLabel(m):
	size = len(m)
	c = 0
	for i in range(size):
		for j in range(size):
			if m[i][j] == 1:
				m[i][j] = chr(ord('a') + c)
				c += 1
			else:
				m[i][j] = None


# def canonicalizeTest4():
# 	m = [
# 		[None, None, None, None, None, None, None, None],
# 		['a', None, None, None, None, None, None, None],
# 		[None, 'b', None, None, None, None, None, None],
# 		[None, None, 'c', None, None, None, None, None],
# 		['d', None, None, None, None, None, None, None],
# 		[None, None, None, None, 'e', None, None, None],
# 		['f', None, None, None, None, None, None, None],
# 		['g', None, None, None, None, None, None, None]]
#
# 	Program.prettyPrint(m)
# 	m2 = Program.canonicalize(m, 2)
# 	Program.prettyPrint(m2)


def canonicalizeTestRandom():
	G = nx.generators.scale_free_graph(8, delta_out=0.1)
	A = nx.adjacency_matrix(G)
	m = A.toarray().tolist()
	assignEdgeLabel(m)

	Program.showGraph(m, False)
	m2 = Program.canonicalize(m, 2)
	Program.prettyPrint(m2)
	Program.showGraph(m2, False)


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

	assert hash1 == hash2, 'Isomorphic graphs gave different hash.'


if __name__ == '__main__':
	canonicalizeTestRandom()
