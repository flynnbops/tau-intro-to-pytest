import pytest

pytestmark = [pytest.mark.math]


def test_one_plus_one_is_two():
    assert 1 + 1 == 2


def test_one_minus_one_is_zero():
    assert 1 - 1 == 0


def test_one_minus_two_is_negative_one():
    a = 1
    b = 2
    c = -1
    assert a - b == c


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as error:
        1 / 0  # type: ignore

    assert 'division by zero' in str(error.value)


combos = [
    (1, 15, 15),
    (100, 0, 0),
    (-4, -5, 20),
    (-10, 2, -20)
]


@pytest.mark.parametrize('a, b, product', combos)
def test_multiplication(a, b, product):
    assert a * b == product
