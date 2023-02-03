import pytest
from day04.script import script

@pytest.mark.parametrize("key,number,startswith", [("abcdef",609043,"000001dbbfa"),("pqrstuv",1048970,"000006136ef")])
def test_get_hash_hexdigest(key, number, startswith):
    actual = script().get_hash_hexdigest(key,number)
    assert actual.startswith(startswith)

@pytest.mark.parametrize("key,startswith,expected", [("abcdef","0" * 5,609043),("pqrstuv","0" * 5,1048970)])
def test_find_number_for_hash_startswith(key, startswith, expected):
    actual = script().find_number_for_hash_startswith(key,startswith)
    assert actual == expected