import pytest
from day19.script import Script
from common.graph import Graph

input = [
    "H => HO",
    "H => OH",
    "O => HH",
    "",
    "HOHOHO"
]

def test_script_parse_input():
    script = Script()
    actual = script.parse_input(input)
    assert type(actual[0]) is dict
    assert type(actual[1]) is str
    assert actual[0] == {"H":["HO","OH"],"O":["HH"]}
    assert actual[1] == "HOHOHO"

@pytest.mark.parametrize('input,expected', [
    ('HOH',['H','O','H']),
    ('HOHOHO',['H','O','H','O','H','O']),
    ('e',['e']),
])
def test_script_split_medicine(input : str, expected : "list[str]"):
    script = Script()
    actual = script.split_medicine(input)
    assert actual == expected

@pytest.mark.parametrize('formula,replacements,expected', [
    (['H','O','H'],{"H":["HO","OH"],"O":["HH"]},{"HOOH","HOHO","OHOH","HHHH"}),
    (['H','_','O','_','H'],{"H":["HO","OH"],"O":["HH"]},{"HO_O_H","OH_O_H","H_HH_H","H_O_HO","H_O_OH"}),
    (['H','O','H','O','H','O'],{"H":["HO","OH"],"O":["HH"]},{'HOHHHHO','OHOHOHO','HOHOHHH','HOHOHOO','HHHHOHO','HOOHOHO','HOHOOHO'}),
])
def test_script_generate_one_off_molecules(formula : "list[str]", replacements : dict, expected : set):
    script = Script()
    actual = script.generate_one_off_molecules(formula, replacements)
    assert actual == expected

@pytest.mark.parametrize('formula,replacements,expected', [
    (['H','O','H'],{"H":["HO","OH"],"O":["HH"]},{"HOH","HOOH","HOHO","OHOH","HHHH","HOHHH","OHHHH","HHHHO","HHHOH","HOOHO","HOOOH","OHOHO","OHOOH","HOHHHO","HOHHOH","OHHHHO","OHHHOH"}),
])
def test_script_generate_all_molecules(formula : "list[str]", replacements : dict, expected : set):
    molecules = set()
    script = Script()
    script.generate_all_molecules(formula, replacements, molecules)
    assert molecules == expected