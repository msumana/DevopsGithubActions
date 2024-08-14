# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

def subtract(a, b):
    return a - b

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(1, -1) == 2
