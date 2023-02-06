import pytest
from day07.script import Script

@pytest.mark.parametrize("instruction,code", [
    ("123 -> x","def _x() : return 123"),
    ("456 -> y","def _y() : return 456"),
    ("x AND y -> d","def _d() : return _x() & _y()"),
    ("x OR y -> e","def _e() : return _x() | _y()"),
    ("x LSHIFT 2 -> f","def _f() : return _x() << 2"),
    ("y RSHIFT 2 -> g","def _g() : return _y() >> 2"),
    ("NOT x -> h","def _h() : return ~_x() + 2**16"),
    ("NOT y -> i","def _i() : return ~_y() + 2**16"),
    ("1 AND x -> y","def _y() : return 1 & _x()"),
    ("x -> y","def _y() : return _x()")
])
def test_script_get_code_from_instruction(instruction : str, code : str):
    script = Script()
    actual = script.get_code_from_instruction(instruction)
    assert actual == code

def test_script_circuit():
    script = Script()
    instructions = [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i"
    ]
    for instruction in instructions:
        code = script.get_code_from_instruction(instruction)
        exec(code,globals())
    local = {}
    exec("actual = _d()",globals(),local)
    assert local['actual'] == 72
    exec("actual = _e()",globals(),local)
    assert local['actual'] == 507
    exec("actual = _f()",globals(),local)
    assert local['actual'] == 492
    exec("actual = _g()",globals(),local)
    assert local['actual'] == 114
    exec("actual = _h()",globals(),local)
    assert local['actual'] == 65412
    exec("actual = _i()",globals(),local)
    assert local['actual'] == 65079
    exec("actual = _x()",globals(),local)
    assert local['actual'] == 123
    exec("actual = _y()",globals(),local)
    assert local['actual'] == 456