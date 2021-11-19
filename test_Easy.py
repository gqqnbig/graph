import pytest

import Program
import Easy


@pytest.mark.timeout(5)
def test_SameChildren():
	m = [
		[None, None, None, 'a', 'a', None, None],
		[None, None, None, None, None, None, None],
		[None, None, None, None, None, None, 'c'],
		[None, None, None, None, None, 'b', None],
		[None, None, 'b', None, None, None, None],
		[None, 'c', None, None, None, None, None],
		[None, None, None, None, None, None, None]
	]

	# Program.showGraph(m, True)

	l = [0]
	Easy.canonicalize(m, l)
	assert l[1] == 3 or l[1] == 4, '0 points to 3 and 4, and 3,4 are identical. We can choose either.'


@pytest.mark.timeout(5)
def test_SelfLoop():
	m = [
		[None, None, None, 'a', 'a', None, None],
		[None, 'e', None, None, None, None, None],
		[None, None, None, None, None, None, 'c'],
		[None, None, None, None, None, 'b', None],
		[None, None, 'b', None, None, None, None],
		[None, 'c', None, None, None, None, None],
		[None, None, None, None, None, None, 'e']
	]

	# Program.showGraph(m, True)

	l = [0]
	Easy.canonicalize(m, l)
	assert l[1] == 3 or l[1] == 4, '0 points to 3 and 4, and 3, 4 are identical. We can choose either.'


@pytest.mark.timeout(5)
def test_LongLoopToKnownHeterogeneous():
	m = [
		[None, None, None, 'a', 'a', None, None],
		['d', None, None, None, None, None, None],
		[None, None, None, None, None, None, 'c'],
		[None, None, None, None, None, 'b', None],
		[None, None, 'b', None, None, None, None],
		[None, 'c', None, None, None, None, None],
		['a', None, None, None, None, None, None]
	]

	# Program.showGraph(m, True)

	l = [0]
	Easy.canonicalize(m, l)
	assert l == [0, 4, 2, 6, 3, 5, 1], '[0]-a->[4]-b->[2]-c->[6]-a->[0], 6 goes to 0 via a, which is smaller than 1. Thus 4 should be the smallest node.'

@pytest.mark.timeout(5)
def test_LongLoopToKnownHomogeneous():
	m = [
		[None, None, None, 'a', 'a', None, None],
		['d', None, None, None, None, None, None],
		[None, None, None, None, None, None, 'c'],
		[None, None, None, None, None, 'b', None],
		[None, None, 'b', None, None, None, None],
		[None, 'c', None, None, None, None, None],
		['d', None, None, None, None, None, None]
	]

	# Program.showGraph(m, True)

	l = [0]
	Easy.canonicalize(m, l)
	assert l[1] == 3 or l[1] == 4, '0 points to 3 and 4, and 3, 4 are identical. We can choose either.'

if __name__ == '__main__':
	test_SameChildren()
