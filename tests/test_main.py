from src.main import addition, subtract


def test_add():
    assert addition(2, 3) == 5
    assert addition(0, 0) == 0
    assert addition(5, 5) == 10

def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(0, 0) == 0
    assert subtract(10, 5) == 5 