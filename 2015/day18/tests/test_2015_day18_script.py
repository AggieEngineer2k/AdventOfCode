import pytest
from day18.script import Script
from common.coordinate import Coordinate

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

# For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:
# 
# 1B5...
# 234...
# ......
# ..123.
# ..8A4.
# ..765.

@pytest.mark.parametrize('row,column,height,width,expected', [
    (0,1,6,6,[(0,0),(1,0),(1,1),(1,2),(0,2)]),
    (4,3,6,6,[(3,2),(3,3),(3,4),(4,4),(5,4),(5,3),(5,2),(4,2)])
])
def test_script_get_neighbor_indexes(row : int, column : int, height : int, width : int, expected : "list[tuple]"):
    script = Script()
    actual = script.get_neighbor_indexes(row, column, height, width)
    assert sorted(actual) == sorted(expected)

# Initial state
# .#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####..
array_step_0 = [
    [False,True,False,True,False,True],
    [False,False,False,True,True,False],
    [True,False,False,False,False,True],
    [False,False,True,False,False,False],
    [True,False,True,False,False,True],
    [True,True,True,True,False,False]
]

# After 1 step:
# ..##..
# ..##.#
# ...##.
# ......
# #.....
# #.##..
array_step_1 = [
    [False,False,True,True,False,False],
    [False,False,True,True,False,True],
    [False,False,False,True,True,False],
    [False,False,False,False,False,False],
    [True,False,False,False,False,False],
    [True,False,True,True,False,False]
]

# After 2 steps:
# ..###.
# ......
# ..###.
# ......
# .#....
# .#....
array_step_2 = [
    [False,False,True,True,True,False],
    [False,False,False,False,False,False],
    [False,False,True,True,True,False],
    [False,False,False,False,False,False],
    [False,True,False,False,False,False],
    [False,True,False,False,False,False]
]

# After 3 steps:
# ...#..
# ......
# ...#..
# ..##..
# ......
# ......
array_step_3 = [
    [False,False,False,True,False,False],
    [False,False,False,False,False,False],
    [False,False,False,True,False,False],
    [False,False,True,True,False,False],
    [False,False,False,False,False,False],
    [False,False,False,False,False,False]
]

# After 4 steps:
# ......
# ......
# ..##..
# ..##..
# ......
# ......
array_step_4 = [
    [False,False,False,False,False,False],
    [False,False,False,False,False,False],
    [False,False,True,True,False,False],
    [False,False,True,True,False,False],
    [False,False,False,False,False,False],
    [False,False,False,False,False,False]
]

@pytest.mark.parametrize('row,column,array,expected', [
    (0,1,array_step_0,[False,False,False,False,False]),
    (4,3,array_step_0,[True,False,False,False,False,True,True,True]),
])
def test_script_get_neighbor_values(row : int, column : int, array : "list[list[bool]]", expected : "list[bool]"):
    script = Script()
    actual = script.get_neighbor_values(row, column, array)
    assert sorted(actual) == sorted(expected)

@pytest.mark.parametrize('array,expected', [
    (array_step_0,array_step_1),
    (array_step_1,array_step_2),
    (array_step_2,array_step_3),
    (array_step_3,array_step_4),
])
def test_script_get_new_array(array : "list[list[bool]]", expected : "list[list[bool]]"):
    script = Script()
    actual = script.get_new_array(array)
    assert sorted(actual) == sorted(expected)