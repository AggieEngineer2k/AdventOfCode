import pytest
from Day02.script import script, Present

@pytest.mark.parametrize("input,expected", [("1x2x3",Present(1,2,3)),("3x2x1",Present(3,2,1))])
def test_get_Present_from_dimensions(input, expected : Present):
    solver = script()
    actual = solver.get_Present_from_dimensions(input)
    print(f"{input} -> {actual} = {expected}")
    assert actual == expected