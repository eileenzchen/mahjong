import random
from Tile import Tile
from Player import Player
mainSuites = ["Bamboo", "Character", "Circles"]
specialSuites = [["Wind", ("North", "East", "South", "West")], ["Dragon", ("Red", "Green", "Black")]]
pointSuites = ["Flower", "Season"] 
class Game(object):
	def __init__(self):
		self.currentPlayer = 0 
		self.players = []
		#back of the tileDeck is actually the front cause  .pop is faster than .pop(0)
		self.tileDeck = []
		self.discardPile = []

	def generateDeck(self):
		#bamboos characters and circleboys
		for ms in mainSuites:
			#[1,9] on tiles for mainsuites
			for i in range(1,10):
				#4 of each tile
				for j in range(4):
					self.tileDeck.append(Tile(ms,i))
		#the lesser kind
		for pair in specialSuites:
			suite, values = pair
			for val in values:
				for i in range(4):
					self.tileDeck.append(Tile(suite, val))

		#the reroll kind
		for pS in pointSuites:
			for i in range(4):
				self.tileDeck.append(Tile(pS, i+1))
	def shuffleDeck(self):
		#we shuffle twice here
		random.shuffle(self.tileDeck)
		random.shuffle(self.tileDeck)

	def rollDice(self):
		return (random.randint(1,6) + random.randint(1,6) + random.randint(1,6))

	def restart(self):
		self.tileDeck = []
		self.discardPile = []
		self.generateDeck()
		self.shuffleDeck()

	def addPlayer(self, playerName):
		self.players.append(Player(playerName))

	def startGame(self):
		assert(len(self.players)==4)
		self.restart()
		diceRoll = self.rollDice()
		print("Dice roll is " + str(diceRoll))
		self.currentPlayer = diceRoll%4
		'''ctr = 0
		while ctr<4:
			currPlayer = self.players[self.currentPlayer]
			#get 4 tiles and then next player
			for j in range(4):
				currPlayer.addToHand(self.tileDeck.pop())
				print(currPlayer)
			self.currentPlayer = (self.currentPlayer+1)%4
			ctr +=1
		'''






test = Game()
test.addPlayer("Helmond")
test.addPlayer("MereHuang")
test.addPlayer("Tim")
test.addPlayer("Eileen")
test.startGame()
for tile in test.tileDeck:
	print(tile)
#for i in range(4):
#	print(test.players[i])





