import pytest
from day20.script import Script

@pytest.mark.parametrize('house,expected', [
    (1,10),
    (2,30),
    (3,40),
    (4,70),
    (5,60),
    (6,120),
    (7,80),
    (8,150),
    (9,130),
])
def test_script_presents(house : int, expected : int):
    script = Script()
    actual = script.presents(house)
    assert actual == expected