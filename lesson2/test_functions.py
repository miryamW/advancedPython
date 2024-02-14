import pytest
from functions import *


def test_find_primes():
    assert find_primes(6) == [2, 3, 5]


@pytest.mark.notcorrect
def test_find_primes():
    assert find_primes(6) == [2, 4, 5]


@pytest.mark.skip(reason="not useable")
def test_find_primes():
    assert find_primes() == []


def test_sort_list():
    assert sort_list([2, 4, 3]) == [2, 3, 4]


@pytest.mark.notcorrect
def test_sort_list():
    assert sort_list([2, 2, 2]) == [2, 2, 3]


@pytest.mark.parametrize("list_num,result", [([1, 3, 4, 5]), ([1, 3, 4, 5])])
def test_sort_list(list_num, result):
    assert sort_list(list_num) == result


def calculate_expression():
    assert calculate_expression('abc') == 6


@pytest.mark.parametrize("str", " [1, 3, 4, 5]")
def calculate_expression():
    assert calculate_expression('abc') == 6


@pytest.mark.skip(reason="not useable")
def calculate_expression():
    assert calculate_expression('abc') == 6
