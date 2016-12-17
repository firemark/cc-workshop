def fizzbuzz(number, fizz='Fizz', buzz='Buzz'):
    if (number % 3 == 0 and number % 5 == 0):
        return fizz + buzz
    elif (number % 3 == 0):
        return fizz
    elif (number % 5 == 0):
        return buzz
    else:
        return str(number)

def print_fizzbuzz(count, fizz='Fizz', buzz='Buzz'):
    return_string = ''
    for i in range(1, count + 1):
        return_string += fizzbuzz(i, fizz, buzz) + '\n'
    return return_string
