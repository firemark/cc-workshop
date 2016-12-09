def fib(n):
    if n in (0, 1):
        return n
    return fib(n-1) + fib(n-2)

print 'Hai guyz'

def fib_wtf(n):
    if n == 0:
        return 11
    elif n == 1:
        return 42
    else:
        return fib_wtf(n-1) + fib_wtf(n-2)

if __name__ == "__main__":
    from sys import argv
    print fib(int(argv[1]))

