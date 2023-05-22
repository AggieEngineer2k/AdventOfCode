import pytest
from day14.script import Script,Reindeer

@pytest.mark.parametrize('input,expected', [
    ('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',Reindeer('Comet',14,10,127)),
    ('Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.',Reindeer('Dancer',16,11,162)),
])
def test_Reindeer_init(input : str, expected : Reindeer):
    actual = Reindeer(input = input)
    assert actual == expected

@pytest.mark.parametrize('reindeer,time,expected', [
    (Reindeer('Comet',14,10,127),1000,1120),
    (Reindeer('Dancer',16,11,162),1000,1056),
])
def test_Reindeer_distance_traveled(reindeer : Reindeer, time : int, expected : int):
    actual = reindeer.distance_traveled(time)
    assert actual == expected