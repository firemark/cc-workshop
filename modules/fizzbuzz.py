def fizzbuzz(n,fizz='fizz',buzz='buzz'):
    x=''
    for i in range(1,n+1):
        if (i%3==0 and i%5!=0):
            x+=fizz
            x+='\n'
        elif (i%5==0 and i%3!=0):
            x+=buzz
            x+='\n'
        elif (i%5==0 and i%3==0):
            x+=fizz
            x+=buzz
            x+='\n'
        else:
            x+=str(i)
            x+='\n'
    return x

print fizzbuzz(20,'ziemniak','kartofel')