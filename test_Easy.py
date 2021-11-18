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


if __name__ == '__main__':
	test_SameChildren()
