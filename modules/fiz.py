def fizzbuzz(n,f="Fizz",b="Buzz"):
    if n==0: return ""
    x="1"
    for i in range(2,n+1):
        x+="\n"
        if i%3==0 and i%5==0:
            x=x+f+b
        elif i%3==0:
            x+=f
        elif i%5==0:
            x+=b
        else:
            x+=str(i)

    return x
