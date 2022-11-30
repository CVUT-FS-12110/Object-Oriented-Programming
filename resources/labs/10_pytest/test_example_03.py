import pytest
from example_03 import ExampleCls

def test_default_value():
    example = ExampleCls()
    assert example.get_value() == 0

def test_set_value():
    example = ExampleCls()
    example.set_value(10.000001)
    assert example.get_value() == pytest.approx(10)

def test_error():
    example = ExampleCls()
    with pytest.raises(ZeroDivisionError):
        result = 1/example.get_value()



    