import pytest
from day02.script import script, Present

@pytest.mark.parametrize("input,expected", [("1x2x3",Present(1,2,3)),("3x2x1",Present(3,2,1)),("12x23x34",Present(12,23,34))])
def test_get_Present_from_dimensions(input, expected : Present):
    solver = script()
    actual = solver.get_Present_from_dimensions(input)
    assert actual == expected

@pytest.mark.parametrize("input,expected", [(Present(1,1,1),7),(Present(2,3,4),58),(Present(1,1,10),43)])
def test_get_square_feet(input : Present, expected : int):
    actual = input.get_square_feet()
    assert actual == expected

@pytest.mark.parametrize("input,expected", [(Present(1,1,1),5),(Present(2,3,4),34),(Present(1,1,10),14)])
def test_get_ribbon_length(input : Present, expected : int):
    actual = input.get_ribbon_length()
    assert actual == expected