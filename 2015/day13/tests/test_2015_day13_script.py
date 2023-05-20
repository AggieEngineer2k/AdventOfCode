import pytest
from day13.script import Script
from common.graph import Graph

@pytest.mark.parametrize('input,expected', [
    ('Alice would gain 54 happiness units by sitting next to Bob.',('Alice','Bob',54)),
    ('Alice would lose 79 happiness units by sitting next to Carol.',('Alice','Carol',-79)),
    ('Alice would lose 2 happiness units by sitting next to David.',('Alice','David',-2)),
    ('Bob would gain 83 happiness units by sitting next to Alice.',('Bob','Alice',83)),
    ('Bob would lose 7 happiness units by sitting next to Carol.',('Bob','Carol',-7)),
    ('Bob would lose 63 happiness units by sitting next to David.',('Bob','David',-63)),
    ('Carol would lose 62 happiness units by sitting next to Alice.',('Carol','Alice',-62)),
    ('Carol would gain 60 happiness units by sitting next to Bob.',('Carol','Bob',60)),
    ('Carol would gain 55 happiness units by sitting next to David.',('Carol','David',55)),
    ('David would gain 46 happiness units by sitting next to Alice.',('David','Alice',46)),
    ('David would lose 7 happiness units by sitting next to Bob.',('David','Bob',-7)),
    ('David would gain 41 happiness units by sitting next to Carol.',('David','Carol',41)),
])
def test_parse_edge(input : str, expected : tuple):
    script = Script()
    actual = script.parse_edge(input)
    assert actual == expected

@pytest.fixture
def input():
    return [
        'Alice would gain 54 happiness units by sitting next to Bob.',
        'Alice would lose 79 happiness units by sitting next to Carol.',
        'Alice would lose 2 happiness units by sitting next to David.',
        'Bob would gain 83 happiness units by sitting next to Alice.',
        'Bob would lose 7 happiness units by sitting next to Carol.',
        'Bob would lose 63 happiness units by sitting next to David.',
        'Carol would lose 62 happiness units by sitting next to Alice.',
        'Carol would gain 60 happiness units by sitting next to Bob.',
        'Carol would gain 55 happiness units by sitting next to David.',
        'David would gain 46 happiness units by sitting next to Alice.',
        'David would lose 7 happiness units by sitting next to Bob.',
        'David would gain 41 happiness units by sitting next to Carol.',
    ]

def test_build_graph(input):
    script = Script()
    actual = script.build_graph(input)
    assert actual.dictionary == {
        "Alice":{
            "Bob":54,
            "Carol":-79,
            "David":-2
        },
        "Bob":{
            "Alice":83,
            "Carol":-7,
            "David":-63
        },
        "Carol":{
            "Alice":-62,
            "Bob":60,
            "David":55
        },
        "David":{
            "Alice":46,
            "Bob":-7,
            "Carol":41
        },
    }

def test_total_happiness(input):
    script = Script()
    seating_arrangement = ['Alice','Bob','Carol','David']
    graph = script.build_graph(input)
    actual = script.total_happiness(seating_arrangement, graph)
    assert actual == 330

def test_max_happiness(input):
    script = Script()
    graph = script.build_graph(input)
    actual = script.max_happiness(graph)
    assert actual == 330