import pytest
from day08.script import Script

# "" is 2 characters of code (the two double quotes), but the string contains zero characters.
# "abc" is 5 characters of code, but 3 characters in the string data.
# "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
# "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.

@pytest.mark.parametrize("line,expected", [
    (r'""', 2),
    (r'"abc"', 5),
    (r'"aaa\"aaa"', 10),
    (r'"\x27"', 6),
])
def test_script_get_characters_in_code(line : str, expected : int):
    script = Script()
    actual = script.get_characters_in_code(line)
    assert actual == expected

@pytest.mark.parametrize("line,expected", [
    (r'""', 0),
    (r'"abc"', 3),
    (r'"aaa\"aaa"', 7),
    (r'"\x27"', 1),
])
def test_script_get_characters_in_memory(line : str, expected : int):
    script = Script()
    actual = script.get_characters_in_memory(line)
    assert actual == expected

# For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.
def test_script_get_difference_of_characters_in_code_and_memory():
    lines = [
        r'""',
        r'"abc"',
        r'"aaa\"aaa"',
        r'"\x27"',
    ]
    script = Script()
    actual = script.get_difference_of_characters_in_code_and_memory(lines)
    assert actual == 12