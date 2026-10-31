import pytest
from calculator import add, subtract, multiply, divide, square_root


def test_add():
    assert add(2, 3) == 6


def test_subtract():
    assert subtract(10, 4) == 5


def test_multiply():
    assert multiply(6, 7) == 42


def test_divide():
    assert divide(20, 5) == 4


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_square_root():
    assert square_root(9) == 3


def test_square_root_negative():
    with pytest.raises(ValueError):
        square_root(-4)