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

# "" encodes to "\"\"", an increase from 2 characters to 6.
# "abc" encodes to "\"abc\"", an increase from 5 characters to 9.
# "aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
# "\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11.

@pytest.mark.parametrize("line,expected", [
    (r'""', r'"\"\""'),
    (r'"abc"', r'"\"abc\""'),
    (r'"aaa\"aaa"', r'"\"aaa\\\"aaa\""'),
    (r'"\x27"', r'"\"\\x27\""'),
])
def test_script_get_encoded(line : str, expected : str):
    script = Script()
    actual = script.get_encoded(line)
    assert actual == expected

@pytest.mark.parametrize("line,expected", [
    (r'""', 6),
    (r'"abc"', 9),
    (r'"aaa\"aaa"', 16),
    (r'"\x27"', 11),
])
def test_script_get_characters_in_encoded(line : str, expected : int):
    script = Script()
    actual = script.get_characters_in_encoded(line)
    assert actual == expected

# For example, for the strings above, the total encoded length (6 + 9 + 16 + 11 = 42) minus the characters in the original code representation (23, just like in the first part of this puzzle) is 42 - 23 = 19.
def test_script_get_difference_of_characters_in_encoded_and_original():
    lines = [
        r'""',
        r'"abc"',
        r'"aaa\"aaa"',
        r'"\x27"',
    ]
    script = Script()
    actual = script.get_difference_of_characters_in_encoded_and_original(lines)
    assert actual == 19