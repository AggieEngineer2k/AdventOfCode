import pytest
from day21.script import Script,Combatant

@pytest.mark.parametrize('input,expected', [
    (['Hit Points: 100','Damage: 8','Armor: 2'],Combatant(100,8,2)),
])
def test_script_parse_input(input : "list[str]", expected : Combatant):
    script = Script()
    actual = script.parse_input(input)
    assert actual == expected

@pytest.mark.parametrize('combatant,opponent,expected', [
    (Combatant(8,5,5),Combatant(12,7,2),True),
])
def test_Combatant_wins_against(combatant : Combatant, opponent : Combatant, expected : bool):
    actual = combatant.wins_against(opponent)
    assert actual == expected