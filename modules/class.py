class Figura(object):
    def __init__(self,katy):
        self.katy = katy 
    def pole(self):
        pass
    def obwod(self):
        pass
class Czworokat(Figura):
    def __init__(self,katy,a,b,c,d,h):
        self.katy = 4
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h
    def obwod(self):
        return self.a+self.b+self.c+self.d

class Trojkat(Figura):
    def __init__(self,katy,a,b,c,h):
        self.katy=3
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def pole(self,a,h):
        return 0.5*a*h
    def obwod(self,a,b,c):
        return a+b+c

class Trapez(Czworokat):
    def __init__(self,katy,a,b,c,d,h):
        self.katy = 4
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h
    def pole(self):
        return 0.5*(self.a+self.b)*self.h

class Prostokat(Czworokat):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def obwod(self):
        return 2*(self.a+self.b)
    def pole(self):
        return self.a*self.b

class Kwadrat(Prostokat):
    def __init__(self,a):
        self.a = a
    def obwod(self):
        return 4*self.a
    def pole(self):
        return self.a**2

class Kwadrat2(Prostokat):
    def __init__(self,a):
        super(Kwadrat2,self).__init__(a,a)

x=Kwadrat(3)
print x.pole()
print x.obwod()

k=Kwadrat2(3)
print k.pole(), k.obwod()

t=Trapez(4,1,2,5,8,4)
print t.pole(), t.obwod()