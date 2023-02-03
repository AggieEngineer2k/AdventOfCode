import pytest
from day03.script import Santa

@pytest.mark.parametrize("input,expected", [("^",(0,1)),(">",(1,0)),("v",(0,-1)),("<",(-1,0))])
def test_Santa_move(input, expected):
    santa = Santa()
    actual = santa.move(input)
    assert actual == expected

@pytest.mark.parametrize("input,expected", [
    ("^",           list(((0,0),(0,1)))),
    ("^v",          list(((0,0),(0,1),(0,0)))),
    ("^v>",         list(((0,0),(0,1),(0,0),(1,0)))),
    ("^v><",        list(((0,0),(0,1),(0,0),(1,0),(0,0)))),
    ("^v><v",       list(((0,0),(0,1),(0,0),(1,0),(0,0),(0,-1)))),
    ("^v><v^",      list(((0,0),(0,1),(0,0),(1,0),(0,0),(0,-1),(0,0)))),
    ("^v><v^<",     list(((0,0),(0,1),(0,0),(1,0),(0,0),(0,-1),(0,0),(-1,0)))),
    ("^v><v^<>",    list(((0,0),(0,1),(0,0),(1,0),(0,0),(0,-1),(0,0),(-1,0),(0,0)))),
])
def test_Santa_every_house(input, expected : list):
    santa = Santa()
    [santa.move(i) for i in input]
    actual = santa.houses
    assert actual == expected

@pytest.mark.parametrize("input,expected", [
    (">",2),
    ("^>v<",4),
    ("^v^v^v^v^v",2)
])
def test_Santa_get_number_of_visited_houses(input, expected):
    santa = Santa()
    [santa.move(i) for i in input]
    actual = santa.get_number_of_visited_houses()
    assert actual == expected
