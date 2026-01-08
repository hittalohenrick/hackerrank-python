from function import is_leap 

def test_is_leap():
    assert is_leap(1800) == False
    assert is_leap(1900) == False
    assert is_leap(1990) == False
    assert is_leap(2000) == True
    assert is_leap(2100) == False
    assert is_leap(2200) == False
    assert is_leap(2300) == False
    assert is_leap(2500) == False