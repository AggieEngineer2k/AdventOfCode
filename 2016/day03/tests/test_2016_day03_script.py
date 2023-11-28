import pytest
from day03.script import Script

@pytest.mark.parametrize("input,expected", [
    ("785  516  744",[785,516,744])
])
def test_script_parseLine(input : str, expected : "list(int)"):
    script = Script()
    actual = script.parseLine(input)
    assert actual == expected

@pytest.mark.parametrize("input,expected", [
    ([5,10,25],False),
    ([101,102,103],True)
])
def test_script_parseLine(input : "list(int)", expected : bool):
    script = Script()
    actual = script.isTriangle(input)
    assert actual == expected