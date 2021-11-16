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


if __name__ == '__main__':
	canonicalizeTest3()
