from fiz import fizzbuzz

def test_fizz_1():
    assert fizzbuzz(1,)=="1"

def test_fizz_2():
    assert fizzbuzz(2)=="1\n2"

def test_fizz_3_addition():
    assert fizzbuzz(3,"Tom","Bob")=="1\n2\nTom"

def test_fizz_3():
    assert fizzbuzz(3)=="1\n2\nFizz"

def test_fizz_5_addition():
    assert fizzbuzz(5)=="1\n2\nFizz\n4\nBuzz"

def test_fizz_5():
    assert fizzbuzz(5,"Tom","Bob")=="1\n2\nTom\n4\nBob"
