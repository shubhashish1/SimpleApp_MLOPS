import pytest

def test_fun1():
    a=3
    b=2
    assert True

def fun2(): # This will not run as there is not test_ there in the function starting
    a=3
    b=3
    assert True

def test_fun3():
    a=5
    b=5
    assert True