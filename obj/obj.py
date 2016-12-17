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

class Kwadrad(Prostokat):

class Trapez(Czworokat):