class DynamicLib:
	def kw_from_dynamiclib(self, name, args):
		if name == 'Dynamic 1':
			print name, args
		else:
			print 'UNIMPLEMENTED ', name, args

class Lib2:
	def kw_from_lib2(self):
		print 'this is a kw from lib2'