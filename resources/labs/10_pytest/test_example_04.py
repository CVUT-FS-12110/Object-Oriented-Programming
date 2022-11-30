import pytest
from example_04 import ExampleCls

# Setup of class for testing is here
@pytest.fixture
def example():
    return ExampleCls()

# tests are here without class setup
def test_default_value(example):
    assert example.get_value() == 0

def test_set_value(example):
    example.set_value(10.000001)
    assert example.get_value() == pytest.approx(10)

def test_error(example):
    with pytest.raises(ZeroDivisionError):
        result = 1/example.get_value()



    