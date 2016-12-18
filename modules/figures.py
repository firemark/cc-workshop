class Figura(object):

    def pole(self):
        raise NotImplementedError("pole")

    def obwod(self):
        raise NotImplementedError("obwod")


class Czworokat(Figura):
    katy = 4


class Trojkat(Figura):
    katy = 3

    def __init__(self, a, h):
        self.a = a
        self.h = h

    def pole(self):
        return 0.5 * self.a * self.h


class Prostokat(Czworokat):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return 2 * self.a + 2 * self.b


class Trapez(Czworokat):

    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def pole(self):
        return 0.5 * (self.a + self.b) * self.h


class Kwadrat(Prostokat):

    def __init__(self, a):
        super(Kwadrat, self).__init__(a, a)
