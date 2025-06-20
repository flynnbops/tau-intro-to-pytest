import pytest
from stuff.accum import Accumulator


@pytest.fixture
def accum():
    accum = Accumulator()
    return accum


# Scope is same as accum
@pytest.fixture
def accum1(scope='function'):
    accum = Accumulator()
    return accum


@pytest.fixture
def accum2():
    print('Before yield: Setup for fixture')
    yield Accumulator()
    print('After yield: Teardown for fixture')


@pytest.fixture
# Make use of session to do something in a test run
def accum3(scope='session'):
    print('Before yield: Setup for fixture')
    yield Accumulator()
    print('After yield: Teardown for fixture')
