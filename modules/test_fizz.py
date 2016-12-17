from modules.fizzbuzz import fizzbuzz 
def test_one():
    assert fizzbuzz(1,'ziemniak','kartofel')=='1\n'

def test_fizz():
    assert fizzbuzz(3,'a','b')=='1\n2\na\n'

def test_buzz():
    assert fizzbuzz(5,'a','b')=='1\n2\na\n4\nb\n'

def test_two():
    assert fizzbuzz(2,'x','y')=='1\n2\n'

def test_fizzbuzz():
    assert fizzbuzz(15,'fizz','buzz')=='1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz\n'