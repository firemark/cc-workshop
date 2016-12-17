def fizzbuzz(n,fizz='Fizz',buzz='Buzz'):
	fb = ''
	for i in range(1,n+1):
		fb += get_str(i,fizz,buzz,i==n)
	return fb

def get_str(i,fizz='Fizz',buzz='Buzz',last=False):
	fb = ''
	if i % 3 == 0 or i % 5 == 0:
		if i % 3 == 0:
			fb += fizz
		if i % 5 == 0:
			fb += buzz
	else:
		fb = str(i)

	if not last and fb != '':
		fb += '\n'

	return fb