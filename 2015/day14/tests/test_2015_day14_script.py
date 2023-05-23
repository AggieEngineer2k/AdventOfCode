import pytest
from day14.script import Script,Reindeer,Race

@pytest.mark.parametrize('input,expected', [
    ('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',Reindeer('Comet',14,10,127)),
    ('Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.',Reindeer('Dancer',16,11,162)),
])
def test_Reindeer_init(input : str, expected : Reindeer):
    actual = Reindeer(input = input)
    assert actual == expected

@pytest.mark.parametrize('reindeer,time,expected', [
    (Reindeer('Comet',14,10,127),1,14),
    (Reindeer('Dancer',16,11,162),1,16),
    (Reindeer('Comet',14,10,127),10,140),
    (Reindeer('Dancer',16,11,162),10,160),
    (Reindeer('Comet',14,10,127),11,140),
    (Reindeer('Dancer',16,11,162),11,176),
    (Reindeer('Comet',14,10,127),12,140),
    (Reindeer('Dancer',16,11,162),12,176),
    (Reindeer('Comet',14,10,127),1000,1120),
    (Reindeer('Dancer',16,11,162),1000,1056),
])
def test_Reindeer_distance_traveled(reindeer : Reindeer, time : int, expected : int):
    actual = reindeer.distance_traveled(time)
    assert actual == expected

@pytest.fixture
def race():
    return Race([
        'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
        'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.',
    ])

@pytest.mark.parametrize('time,expected', [
    (1,{"Dancer":1,"Comet":0}),
    (140,{"Dancer":139,"Comet":1}),
    (1000,{"Dancer":689,"Comet":312}),
])
def test_Race_run_race(race, time : int, expected):
    race.run_race(time)
    for name in expected:
        assert race.racers[name].points == expected[name]