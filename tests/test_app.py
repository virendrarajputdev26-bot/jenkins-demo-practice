import sys
sys.path.append("app")

from app import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(5, 6) == 30

print("All tests passed!")

