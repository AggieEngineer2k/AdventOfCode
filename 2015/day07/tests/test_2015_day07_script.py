import pytest
from day07.script import Script

@pytest.mark.parametrize("instruction,dictionary", [
    ("123 -> x", {"x" : 123}),
    ("456 -> y", {"y" : 456}),
    ("x AND y -> d", {"d" : "x & y"}),
    ("x OR y -> e", {"e" : "x | y"}),
    ("x LSHIFT 2 -> f", {"f" : "x << 2"}),
    ("y RSHIFT 2 -> g", {"g" : "y >> 2"}),
    ("NOT x -> h", {"h" : "~x"}),
    ("NOT y -> i", {"i" : "~y"}),
    ("1 AND x -> y", {"y" : "1 & x"}),
    ("x -> y", {"y" : "x"}),
])
def test_script_get_dictionary_key_value_from_instruction(instruction : str, dictionary : dict):
    script = Script()
    actual = script.get_dictionary_key_value_from_instruction(instruction)
    assert actual == dictionary

def test_script_get_value_for_dictionary_key():
    script = Script()
    instructions = [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i",
    ]
    dictionary = {}
    for instruction in instructions:
        dictionary.update(script.get_dictionary_key_value_from_instruction(instruction))
    assert script.get_value_for_dictionary_key(dictionary, "d") == dictionary["d"] == 72
    assert script.get_value_for_dictionary_key(dictionary, "e") == dictionary["e"] == 507
    assert script.get_value_for_dictionary_key(dictionary, "f") == dictionary["f"] == 492
    assert script.get_value_for_dictionary_key(dictionary, "g") == dictionary["g"] == 114
    assert script.get_value_for_dictionary_key(dictionary, "h") == dictionary["h"] == 65412
    assert script.get_value_for_dictionary_key(dictionary, "i") == dictionary["i"] == 65079
    assert script.get_value_for_dictionary_key(dictionary, "x") == dictionary["x"] == 123
    assert script.get_value_for_dictionary_key(dictionary, "y") == dictionary["y"] == 456