import pytest
from stuff.accum import Accumulator


def test_accum_init(accum):
    assert accum.count == 0


def test_cannot_set_count_directly(accum, accum2):
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter") as e:
        accum.count = 1


@pytest.mark.skip
def test_accum_default_add(accum):
    accum.add()
    assert accum.count == 1


def test_accum_add_one(accum):
    accum = Accumulator()
    accum.add(1)
    assert accum.count == 1


def test_accum_add_zero(accum):
    accum.add(0)
    assert accum.count == 0


def test_accum_add_twice(accum):
    accum.add()
    accum.add(1)
    assert accum.count == 2


def test_accum_add_negative_one(accum):
    accum.add(-1)
    assert accum.count == -1
