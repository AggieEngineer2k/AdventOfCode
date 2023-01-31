import pytest
from script import script

@pytest.mark.parametrize("input,expected", [("(())",0),("()()",0),("(((",3),("(()(()(",3),("))(((((",3),("())",-1),("))(",-1),(")))",-3),(")())())",-3)])
def test_determine_floor(input, expected):
    solver = script("")
    assert solver.determine_floor(input) == expected

@pytest.mark.parametrize("input,expected", [(")",1),("())",3)])
def test_determine_instruction_that_enters_basement(input, expected):
    solver = script("")
    assert solver.determine_instruction_that_enters_basement(input) == expected