import pytest
from day05.script import script

@pytest.mark.parametrize("string,expected", [
    ("aei",True),
    ("xazegov",True),
    ("aeiouaeiouaeiou",True),
    ("x",False),
])
def test_has_three_vowels(string, expected):
    actual = script().has_three_vowels(string)
    assert actual == expected

@pytest.mark.parametrize("string,expected", [
    ("xx",True),
    ("abcdde",True),
    ("aabbccdd",True),
    ("x",False),
])
def test_has_double_letter(string, expected):
    actual = script().has_double_letter(string)
    assert actual == expected

@pytest.mark.parametrize("string,forbidden,expected", [
    ("x",['ab','cd','pq','xy'],False),
    ("ab",['ab','cd','pq','xy'],True),
    ("cd",['ab','cd','pq','xy'],True),
    ("pq",['ab','cd','pq','xy'],True),
    ("xy",['ab','cd','pq','xy'],True)
])
def test_has_forbidden(string, forbidden, expected):
    actual = script().has_forbidden(string, forbidden)
    assert actual == expected

@pytest.mark.parametrize("string,expected", [
    ("ugknbfddgicrmopn",True),
    ("aaa",True),
    ("jchzalrnumimnmhp",False),
    ("haegwjzuvuyypxyu",False),
    ("dvszwmarrgswjxmb",False)
])
def test_is_nice_day1(string, expected):
    actual = script().is_nice_day1(string)
    assert actual == expected

@pytest.mark.parametrize("string,expected", [
    ("qjhvhtzxzqqjkmpb",True),
    ("xxyxx",True),
    ("uurcxstgmygtbstg",True),
    ("ieodomkazucvgmuy",False)
])
def test_has_repeated_substring(string, expected):
    actual = script().has_repeated_substring(string)
    assert actual == expected

@pytest.mark.parametrize("string,expected", [
    ("qjhvhtzxzqqjkmpb",True),
    ("xxyxx",True),
    ("uurcxstgmygtbstg",False),
    ("ieodomkazucvgmuy",True),
    ("abcdefe",True),
    ("abacdef",True)
])
def test_has_split_letter(string, expected):
    actual = script().has_split_letter(string)
    assert actual == expected

@pytest.mark.parametrize("string,expected", [
    ("qjhvhtzxzqqjkmpb",True),
    ("xxyxx",True),
    ("uurcxstgmygtbstg",False),
    ("ieodomkazucvgmuy",False)
])
def test_is_nice_day2(string, expected):
    actual = script().is_nice_day2(string)
    assert actual == expected