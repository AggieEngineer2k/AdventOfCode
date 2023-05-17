import pytest
from day11.script import Script

# hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
# abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
# abbcegjk fails the third requirement, because it only has one double letter (bb).
# The next password after abcdefgh is abcdffaa.
# The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.

# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on.
# Increase the rightmost letter one step;
#     if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.
@pytest.mark.parametrize("input,expected", [
    ("a","b"),
    ("z","aa"),
    ("xx","xy"),
    ("xy","xz"),
    ("xz","ya"),
    ("ya","yb"),
])
def test_script_increment_string(input : str, expected : str):
    script = Script()
    actual = script.increment_string(input)
    assert actual == expected