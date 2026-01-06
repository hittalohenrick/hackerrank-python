from loop import squared

def test_squared_with_5():
    assert squared(5) == [0, 1, 4, 9, 16]

def test_squared_with_0():
    assert squared(0) == []

def test_squared_with_1():
    assert squared(1) == [0]