import pytest
from day12.script import Script

@pytest.mark.parametrize('input,expected', [
    ('[1,2,3]',[1,2,3]),
    ('{"a":2,"b":4}',[2,4]),
    ('[[[3]]]',[3]),
    ('{"a":{"b":4},"c":-1}',[4,-1]),
    ('{"a":[-1,1]}',[-1,1]),
    ('[-1,{"a":1}]',[-1,1]),
    ('[]',[]),
    ('{}',[]),
])
def test_extract_numbers(input : str, expected : "list[int]"):
    script = Script()
    actual = script.extract_numbers(input)
    assert actual == expected