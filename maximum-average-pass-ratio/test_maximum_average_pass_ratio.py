import pytest
from maximum_average_pass_ratio import Solution

TOLERANCE = 10**-5


def test_example_1():
    classes = [[1, 2], [3, 5], [2, 2]]
    extra_students = 2

    assert 0.78333 == pytest.approx(
        Solution().max_average_ratio(classes, extra_students),
        TOLERANCE)


def test_example_2():
    classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extra_students = 4

    assert 0.53485 == pytest.approx(
        Solution().max_average_ratio(classes, extra_students),
        TOLERANCE)
