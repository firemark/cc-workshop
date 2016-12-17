def fizzbuzz(n):
	ans=''
	number=True
	if n%3 == 0:
		ans+='Fizz'
		number=False
	if n%5==0:
		ans+='Buzz'
		number=False

	if number:
		ans=str(n)

	return ans;

def string_for_print(n):
	string4print=''
	for i in range(n):
		string4print+=fizzbuzz(i+1)+'\n'

	return string4print



