from print_function import print_sequence

def test_print_sequence_with_number_3(capsys):
    print_sequence(3)
    
    captured = capsys.readouterr()
    assert captured.out == "123"

def test_print_sequence_with_number_5(capsys):
    print_sequence(5)
    captured = capsys.readouterr()
    assert captured.out == "12345"

def test_print_sequence_with_number_0(capsys):
    print_sequence(0)
    captured = capsys.readouterr()
    assert captured.out == ""