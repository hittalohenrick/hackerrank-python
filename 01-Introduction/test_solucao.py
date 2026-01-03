from solucao import check_weirdness

def test_impares():
    assert check_weirdness(3) == "Weird"
    assert check_weirdness(29) == "Weird"

def test_pares_pequenos():
    assert check_weirdness(2) == "Not Weird"
    assert check_weirdness(4) == "Not Weird"

def test_pares_medios():
    assert check_weirdness(6) == "Weird"
    assert check_weirdness(18) == "Weird"
    assert check_weirdness(20) == "Weird"

def test_pares_grandes():
    assert check_weirdness(22) == "Not Weird"
    assert check_weirdness(100) == "Not Weird"