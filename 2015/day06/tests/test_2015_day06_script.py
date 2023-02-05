import pytest
from day06.script import Script, Instruction, Point

@pytest.mark.parametrize("instruction,action,from_light,to_light", [
    ("turn on 0,0 through 999,999","turn on",Point(0,0),Point(999,999)),
    ("toggle 0,0 through 999,0","toggle",Point(0,0),Point(999,0)),
    ("turn off 499,499 through 500,500","turn off",Point(499,499),Point(500,500))
])
def test_Instruction_constructor(instruction,action,from_light,to_light):
    instruction = Instruction(instruction)
    assert instruction.action == action
    assert instruction.from_light == from_light
    assert instruction.to_light == to_light

# turn on 0,0 through 999,999 would turn on (or leave on) every light.
def test_script_follow_instruction_day1_turn_on_0_0_through_999_999():
    rows = 1000
    cols = 1000
    script = Script(rows=rows,cols=cols)
    instruction = Instruction("turn on 0,0 through 999,999")
    for row in script.lights:
        for light in row:
            assert light == 0
    script.follow_instruction_day1(instruction)
    for row in script.lights:
        for light in row:
            assert light == 1

# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
def test_script_follow_instruction_day1_toggle_0_0_through_999_0():
    rows = 1000
    cols = 1000
    script = Script(rows=rows,cols=cols)
    instruction = Instruction("toggle 0,0 through 999,0")
    for light in script.lights[0]:
        assert light == 0
    for row in script.lights[1:]:
        for light in row:
            assert light == 0
    script.follow_instruction_day1(instruction)
    for light in script.lights[0]:
        assert light == 1
    for row in script.lights[1:]:
        for light in row:
            assert light == 0
    script.follow_instruction_day1(instruction)
    for light in script.lights[0]:
        assert light == 0
    for row in script.lights[1:]:
        for light in row:
            assert light == 0

# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
def test_script_follow_instruction_day1_turn_off_499_499_through_500_500():
    rows = 1000
    cols = 1000
    script = Script(rows=rows,cols=cols)
    instruction = Instruction("turn on 0,0 through 999,999")
    script.follow_instruction_day1(instruction)
    instruction = Instruction("turn off 499,499 through 500,500")
    script.follow_instruction_day1(instruction)
    for row in range(499,501):
        for col in range(499,501):
            assert script.lights[row][col] == 0

# turn on 0,0 through 0,0 would increase the total brightness by 1.
def test_script_follow_instruction_day2_turn_on_0_0_through_0_0():
    rows = 1000
    cols = 1000
    script = Script(rows=rows,cols=cols)
    instruction = Instruction("turn on 0,0 through 0,0")
    script.follow_instruction_day2(instruction)
    total_brightness = 0
    for row in script.lights:
        for light in row:
            total_brightness += light
    assert total_brightness == 1

# toggle 0,0 through 999,999 would increase the total brightness by 2000000.
def test_script_follow_instruction_day2_turn_on_0_0_through_999_999():
    rows = 1000
    cols = 1000
    script = Script(rows=rows,cols=cols)
    instruction = Instruction("toggle 0,0 through 999,999")
    script.follow_instruction_day2(instruction)
    total_brightness = 0
    for row in script.lights:
        for light in row:
            total_brightness += light
    assert total_brightness == 2000000