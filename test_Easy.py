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

	Easy.canonicalize(m, [0])


if __name__ == '__main__':
	test_SameChildren()
