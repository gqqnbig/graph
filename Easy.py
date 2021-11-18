from typing import List


def getOutgoingEdges(m, n):
	outgoingEdges = [(e, v) for v, e in enumerate(m[n])]
	outgoingEdges = list(filter(lambda e: e[0] is not None, outgoingEdges))
	return outgoingEdges


def getMinSet(s: list):
	arr = [(''.join(t[0]), t) for t in s]

	minKey = min(arr, key=lambda t: t[0])[0]

	res = []
	for a in arr:
		if a[0] == minKey:
			res.append(a[1])

	return res


def formPath(head, nexts):
	if len(nexts) == 0:
		raise Exception('nexts must have at least 1 element')

	paths = [head, nexts[0]]
	for i in range(1, len(nexts)):
		paths.append((nexts[i - 1], nexts[i]))
	return paths


def findMinNext(m, n, l, visitedPaths=None):
	if visitedPaths is None:
		visitedPaths = []
	edges = getOutgoingEdges(m, n)
	edges = list(filter(lambda t: t[1] not in l, edges))
	edges = list(filter(lambda t: (n, t[1]) not in visitedPaths, edges))

	if len(edges) == 0:
		return None
	else:
		# convert to list
		edges = [([a[0]], [a[1]]) for a in edges]
		loop = True
		while True:
			edges = getMinSet(edges)
			if loop:
				if len(edges) > 1:
					loop = False
					for i in range(len(edges)):
						res = findMinNext(m, edges[i][1][-1], l, visitedPaths + formPath(n, edges[i][1]))
						if res is not None:
							edges[i] = (edges[i][0] + res[0], edges[i][1] + res[1])
							loop = True
				else:
					break
			else:
				print(f'From {n}, two branches are identical')
				break
		return edges[0]


def canonicalize(m, l: List[int]):
	loop = True
	while loop:
		loop = False
		i = 0
		while i < len(l):
			r = findMinNext(m, l[i], l)
			if r is not None:
				l.append(r[1][0])
				loop = True

			i += 1

	return l
