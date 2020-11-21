class Tile(object):
	def __init__(self, suite, value):
		self.suite = suite
		self.value = value
	def getHashables(self):
		return (self.suite, self.value)
	def __hash__(self):
		return hash(self.getHashables())
	def __eq__(self, other):
		return  (isinstance(other, Tile) and self.suite==other.suite and self.value==other.value)
	def __repr__(self):
		return f'({self.value}, {self.suite})'