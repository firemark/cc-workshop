def fizzbuzz(n,f="Fizz",b="Buzz"):
    if n==0: return ""
    x="1"
    for i in range(2,n+1):
        x += '\n' + fizzbuzz_single(i,f,b)

    return x

def fizzbuzz_single(i,f,b):
    if i%3==0 and i%5==0:
        return f+b
    elif i%3==0:
        return f
    elif i%5==0:
       return b 
    else:
        return str(i)

def fizzbuzz_array(n,f='Fizz',b='Buzz'):
    l = []
    for i in range(1, n):
        l.append(fizzbuzz_single(n,f,b))
    return l
    #???
