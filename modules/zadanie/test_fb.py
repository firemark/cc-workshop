from fb import fizzbuzz
from fb import string_for_print


def test_fb1():
	assert fizzbuzz(1)=='1'

def test_fb3():
	assert fizzbuzz(3)=='Fizz'

def test_fb5():
	assert fizzbuzz(5)=='Buzz'

def test_fb15():
	assert fizzbuzz(15)=='FizzBuzz'

def test_string_for_print():
	assert string_for_print(6)=='1\n2\nFizz\n4\nBuzz\nFizz\n'
