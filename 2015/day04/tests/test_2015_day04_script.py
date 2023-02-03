import pytest
from day04.script import script

@pytest.mark.parametrize("key,number,startswith", [("abcdef",609043,"000001dbbfa"),("pqrstuv",1048970,"000006136ef")])
def test_Santa_move(key, number, startswith):
    actual = script().get_hash_hexdigest(key,number)
    assert actual.startswith(startswith)