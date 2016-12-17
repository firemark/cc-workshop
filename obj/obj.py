class Figura(object):
	def pole(self):
		raise NotImplementedError
	def obwod(self):
		raise NotImplementedError

class Czworokat(Figura):
	def __init__(self):
		self.angles = 4

class Trojkat(Figura):
	def __init__(self):
		self.angles = 3

class Prostokat(Czworokat):
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def pole(self):
		return a*b
	def obwod(self):
		return 2*a+2*b

class Kwadrad(Prostokat):
	def __init__(self, a):
		self.a = a
	def pole(self):
		return a*a
	def obwod(self):
		return 4*a

class Trapez(Czworokat):
	def __init__(self, a, b, c, h):
		self.a = a
		self.b = b
		self.h = h
	def pole(self):
		return (a+b)/2*h
	def obwod(self):
		return a+b+2*c