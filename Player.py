from Tile import Tile
class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []
		# for the pongs kongs and chows ya feel
		self.declaredTriples = []
	def __repr__(self):
		return f'{self.name} hand is {self.hand}' 
	def addToHand(self, tile):
		self.hand.append(tile)
	def discard(self, index):
		return self.hand.remove(index)

