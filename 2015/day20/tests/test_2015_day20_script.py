import pytest
from day20.script import Script

# input = [
#     "H => HO",
#     "H => OH",
#     "O => HH",
#     "",
#     "HOHOHO"
# ]

# def test_script_parse_input():
#     script = Script()
#     actual = script.parse_input(input)
#     assert type(actual[0]) is dict
#     assert type(actual[1]) is str
#     assert type(actual[2]) is dict
#     assert actual[0] == {"H":["HO","OH"],"O":["HH"]}
#     assert actual[1] == "HOHOHO"
#     assert actual[2] == {"HO":["H"],"OH":["H"],"HH":["O"]}

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