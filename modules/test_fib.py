from modules.fib import fib

def test_fib_zero():
    assert fib(0) == 0 

def test_fib_one():
    assert fib(1) == 1 

def test_fib_three():
    assert fib(3) == 2
    assert fib(3) == fib(1) + fib(2)
    assert fib(3) == fib(1) + fib(1) + fib(0)
