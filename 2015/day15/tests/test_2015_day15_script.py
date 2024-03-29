import pytest
from day15.script import Script,Ingredient

@pytest.mark.parametrize('input,expected', [
    ('Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',Ingredient('Butterscotch',-1,-2,6,3,8)),
    ('Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3',Ingredient('Cinnamon',2,3,-2,-1,3)),
])
def test_Ingredient_init(input : str, expected : Ingredient):
    actual = Ingredient(input = input)
    assert actual == expected

@pytest.mark.parametrize('amounts,ingredients,expected', [
    ([44,56], [Ingredient('Butterscotch',-1,-2,6,3,8),Ingredient('Cinnamon',2,3,-2,-1,3)], 62842880)
])
def test_Script_calculate_score(amounts : "list[int]", ingredients : "list[Ingredient]", expected : int):
    script = Script()
    actual = script.calculate_score(amounts, ingredients)
    assert actual == expected