from src.main import addition


def test_add():
    assert addition(2, 3) == 5
    assert addition(0, 0) == 0
    assert addition(5, 5) == 10