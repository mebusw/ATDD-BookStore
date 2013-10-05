def kw1(arg):
	print 'kw1', arg

def kw2(arg):
	print '*INFO* returning an object'
	return MyObj('China')


class MyObj:
	def __init__(self, country=''):
		self.country = country
	def __str__(self):
		return self.country
	def version(self):
		return '1.0'