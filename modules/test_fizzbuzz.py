from fizzbuzz import fizzbuzz
from fizzbuzz import get_str

def test_fizzbuzz_empty():
	# print 'test_fizzbuzz_empty'
	assert fizzbuzz(0) == ''

def test_fizzbuzz_lines():
	# print 'test_fizzbuzz_lines'
	n = 20
	assert len(fizzbuzz(n).split('\n')) == n

def test_fizzbuzz_fizz():
	n = 20
	f = 'Fizz'
	b = 'Buzz'
	fb = fizzbuzz(n,f,b).split('\n')
	for line_num in range(1,n+1):
		if line_num % 3 == 0:
			assert f in fb[line_num-1]

def test_fizzbuzz_buzz():
	n = 20
	f = 'Fizz'
	b = 'Buzz'
	fb = fizzbuzz(n,f,b).split('\n')
	for line_num in range(1,n+1):
		if line_num % 5 == 0:
			assert b in fb[line_num-1]

def test_fizzbuzz():
	n = 20
	f = 'Fizz'
	b = 'Buzz'
	fb = fizzbuzz(n,f,b).split('\n')
	for line_num in range(1,n+1):
		if line_num % 3 == 0 and line_num % 5 == 0:
			assert fb[line_num-1] == f+b

def test_get_str1():
	assert get_str(0) == 'FizzBuzz\n'

def test_get_str2():
	assert get_str(1) == '1\n'

def test_get_str3():
	assert get_str(3, last=True) == 'Fizz'

def test_get_str4():
	assert get_str(3,fizz='Kartofel', last=True) == 'Kartofel'

def test_get_str5():
	assert get_str(5,fizz='Kartofel', last=True) == 'Buzz'

def test_get_str6():
	assert get_str(5, last=True) == 'Buzz'