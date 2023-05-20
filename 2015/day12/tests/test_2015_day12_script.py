import pytest
from day12.script import Script

@pytest.mark.parametrize('input,expected', [
    ('[1,2,3]',[1,2,3]),
    ('{"a":1, "b":2}',{"a":1,"b":2}),
])
def test_parse_input(input : str, expected):
    script = Script()
    actual = script.parse_input(input)
    assert actual == expected
    
# Part 1
#
# [1,2,3] and {"a":2,"b":4} both have a sum of 6.
# [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
# {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
# [] and {} both have a sum of 0.

@pytest.mark.parametrize('input,expected', [
    ([1,2,3], 6),
    ({"a":2,"b":4}, 6),
    ([[[3]]],3),
    ({"a":{"b":4},"c":-1},3),
    ({"a":[-1,1]},0),
    ([-1,{"a":1}],0),
    ([],0),
    ({},0),
])
def test_iterate(input, expected : int):
    script = Script()
    actual = script.iterate(input)
    assert actual == expected

# Part 2
#
# [1,2,3] still has a sum of 6.
# [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
# {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
# [1,"red",5] has a sum of 6, because "red" in an array has no effect.

@pytest.mark.parametrize('input,expected', [
    ([1,2,3], 6),
    ([1,{"c":"red","b":2},3], 4),
    ({"d":"red","e":[1,2,3,4],"f":5},0),
    ([1,"red",5],6),
])
def test_iterate_skipRed(input, expected : int):
    script = Script()
    actual = script.iterate(input, skipRed=True)
    assert actual == expected