from binaryConverter import decToBinList

def test_normal_case():
    assert decToBinList(25) == [1, 1, 0, 0, 1]

def test_power_of_two():
    assert decToBinList(8) == [1, 0, 0, 0]
    assert decToBinList(16) == [1, 0, 0, 0, 0]

def test_zero_case():
    assert decToBinList(0) == [0]


