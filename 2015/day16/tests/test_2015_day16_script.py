import pytest
from day16.script import Script,Sue

@pytest.mark.parametrize('input,expected', [
    ('Sue 1: goldfish: 9, cars: 0, samoyeds: 9',Sue(number=1,attributes={'goldfish': 9, 'cars': 0, 'samoyeds': 9})),
    ('Sue 2: perfumes: 5, trees: 8, goldfish: 8',Sue(number=2,attributes={'perfumes': 5, 'trees': 8, 'goldfish': 8})),
    ('Sue 3: pomeranians: 2, akitas: 1, trees: 5',Sue(number=3,attributes={'pomeranians': 2, 'akitas': 1, 'trees': 5}))
])
def test_Sue_init(input : str, expected : Sue):
    actual = Sue(input = input)
    assert actual == expected

@pytest.fixture
def input() -> "list[str]":
    return [
        'Sue 1: goldfish: 9, cars: 0, samoyeds: 9',
        'Sue 2: perfumes: 5, trees: 8, goldfish: 8',
        'Sue 3: pomeranians: 2, akitas: 1, trees: 5'
    ]

@pytest.fixture
def aunts() -> "list[Sue]":
    return [
        Sue(number=1,attributes={'goldfish': 9, 'cars': 0, 'samoyeds': 9}),
        Sue(number=2,attributes={'perfumes': 5, 'trees': 8, 'goldfish': 8}),
        Sue(number=3,attributes={'pomeranians': 2, 'akitas': 1, 'trees': 5})
    ]

def test_Script_parse_input(input,aunts):
    script = Script()
    actual = script.parse_input(input)
    assert len(actual) == len(aunts)
    for i in range(len(actual)):
        assert actual[i] == aunts[i]
