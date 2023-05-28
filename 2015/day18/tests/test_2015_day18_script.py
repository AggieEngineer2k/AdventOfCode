import pytest
from day18.script import Script

@pytest.mark.parametrize('input,expected', [
    (['#'],[[True]]),
    (['.'],[[False]]),
    (['#.','.#'],[[True,False],[False,True]]),
    (['#.#','.#.','#.#'],[[True,False,True],[False,True,False],[True,False,True]]),
])
def test_script_parse_input(input : "list[str]", expected : "list[list[bool]]"):
    script = Script()
    actual = script.parse_input(input)
    assert actual == expected