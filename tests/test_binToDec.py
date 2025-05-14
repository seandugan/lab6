from binaryConverter import binToDecList

def test_binToDec():
    assert binToDecList([1, 1, 0, 0, 1]) == 25, "doesn't return correct number, should return 25"

