class HybridLib:
	_kws = ['get_keyword_names', 'hybrid1', 'hybrid2', 'hybrid3', 'hybrid5']

	def get_keyword_names(self):
		return self._kws

	def hybrid1(self):
		print 'H1'

	def hybrid2(self, arg):
		print 'H2', arg

	def __getattr__(self, name):
		if name not in self._kws:
			raise AttributeError
		def keyword(arg):
			print 'UNIMPLEMENTED', name.upper(), arg.upper()
		return keyword
