from modules.fizzbuzz import fizzbuzz
from modules.fizzbuzz import print_fizzbuzz

def test_fizzbuzz_one():
    assert fizzbuzz(1) == '1'

def test_fizzbuzz_three():
    assert fizzbuzz(3) == 'Fizz'

def test_fizzbuzz_three_hey_there():
    assert fizzbuzz(3, 'Hey', 'There') == 'Hey'

def test_fizzbuzz_five():
    assert fizzbuzz(5) == 'Buzz'

def test_fizzbuzz_five_hey_there():
    assert fizzbuzz(5, 'Hey', 'There') == 'There'

def test_fizzbuzz_fifteen():
    assert fizzbuzz(15) == 'FizzBuzz'

def test_print_fizzbuzz_one():
    assert print_fizzbuzz(1) == '1\n'

def test_print_fizzbuzz_two():
    assert print_fizzbuzz(2) == '1\n2\n'

def test_print_fizzbuzz_three_hey_there_plus():
    assert print_fizzbuzz(3, 'Hey', 'There', '+') == '1+2+Hey+'

def test_print_fizzbuzz_five():
    assert print_fizzbuzz(5) == '1\n2\nFizz\n4\nBuzz\n'

def test_print_fizzbuzz_fifteen():
    assert print_fizzbuzz(15) == '1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n'

def test_print_fizzbuzz_fifteen_hey_there():
    assert print_fizzbuzz(15, 'Hey', 'There') == '1\n2\nHey\n4\nThere\nHey\n7\n8\nHey\nThere\n11\nHey\n13\n14\nHeyThere\n'
