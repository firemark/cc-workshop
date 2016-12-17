class Figura(object):
	def pole(self):
		raise NotImplementedError
	def obwod(self):
		raise NotImplementedError

class Czworokat(Figura):
	def __init__(self):
		super(Figura, self).__init__()
		self.angles = 4

class Trojkat(Figura):
	def __init__(self):
		super(Figura, self).__init__()
		self.angles = 3

class Prostokat(Czworokat):
	def __init__(self, a, b):
		super(Czworokat, self).__init__()
		self.a = a
		self.b = b
	def pole(self):
		return self.a*self.b
	def obwod(self):
		return 2*self.a+2*self.b

class Kwadrat(Prostokat):
	def __init__(self, a):
		self.a = a
	def pole(self):
		return self.a*self.a
	def obwod(self):
		return 4*self.a

class Trapez(Czworokat):
	def __init__(self, a, b, c, h):
		super(Czworokat, self).__init__()
		self.a = a
		self.b = b
		self.c = c
		self.h = h
	def pole(self):
		return (self.a+self.b)/2*self.h
	def obwod(self):
		return self.a+self.b+2*self.c