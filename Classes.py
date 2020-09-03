import sys, pygame, random
from pygame.locals import *

class Img:
	def __init__(self, obj, x, y):
		self.obj = obj
		self.x = x
		self.y = y


class Card:
	 def __init__(self, value, suit):  
	
	 	self.value = value
	 	self.suit = suit
	 	self.img = 'f' + str(value) + suit 
	 suit_master = ["hearts", "spades", "clubs", "diamonds"]
	 value_master = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

class Deck:
	def __init__(self):
		self.cards = []
		self.create()

	def create(self):
		#for item in range(number_of_decks):
		for val in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
			for suit_elem in ["hearts", "spades", "clubs", "diamonds"]:
				self.cards.append(Card(val, suit_elem))