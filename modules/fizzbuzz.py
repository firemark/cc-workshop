def fizzbuzz(n,f='fizz',b='buzz'):
    x=''
    for i in range(1,n+1):
        if (i%5==0 and i%3==0):
            x+=f+b
        elif i%3==0:
            x+=f
        elif i%5==0:
            x+=b
        else:
            x+=str(i)
        x+='\n'
    return x

def fizzbuzz_single(i,f,b):
    if (i%5==0 and i%3==0): return f+b
    elif i%3==0: return f
    elif i%5==0: return b
    else: return str(i)


print fizzbuzz(20,'ziemniak','kartofel')