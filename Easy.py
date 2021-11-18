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


def findMinNext(m, n, l):
	s = getOutgoingEdges(m, n)
	s = list(filter(lambda t: t[1] not in l, s))

	if len(s) == 0:
		return None
	else:
		# convert to list
		s = [([a[0]], [a[1]]) for a in s]
		while True:
			s = getMinSet(s)
			if len(s) > 1:
				for i in range(len(s)):
					res = findMinNext(m, s[i][1][-1], l)
					if res is not None:
						s[i] = (s[i][0] + res[0], s[i][1] + res[1])
			else:
				break
		return s[0]


def canonicalize(m, l: List[int]):
	loop = True
	while loop:
		loop = False
		i = 0
		while i < len(l):
			r = findMinNext(m, l[i], l)
			if r is not None:
				l.append(r[1][-1])
				loop = True

			i += 1

	return l
