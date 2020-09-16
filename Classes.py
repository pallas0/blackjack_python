import sys, pygame, random, math
from pygame.locals import *
import pygame_gui

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Img:
	def __init__(self, obj, x, y):
		self.obj = obj
		self.x = x
		self.y = y

	def move(fill_func, blit_func, screen_update_func,
	 screen_obj, second_obj):
		def move_func(self, new_x, new_y):
			#temp, need to fix this
			if new_x > self.x:
				dx = 1
			else:
				dx = -1
			if new_y > self.y:
				dy = 1
			else:
				dy = -1
			if abs(new_x - self.x) >= 0.1:
				self.x += dx*0.2
				if abs(new_y - self.y) >= 0.1:
					self.y += dy*0.2
					fill_func(screen_obj)
			blit_func(self.obj, (self.x, self.y))
			if second_obj:
				blit_func(second_obj.obj, (second_obj.x, second_obj.y))
			screen_update_func()
			return (self.x, self.y)
		return move_func
				# screen.fill(WHITE)
		# while abs(new_x - x) >= 0.001:

		#  	() abs(new_x - x) > 0.001:
		# 	x += dy_dx
		# 	while abs(new_y - y) > 0.001:
		# 		y += dy_dx




class Card:
	 def __init__(self, value, suit):  
	
	 	self.value = value
	 	self.suit = suit
	 	#make the object attribute store its own Img object (right?)
	 	#try rewriting w/ pygame.image.load("string.type").convert()
	 	self.img = 'f' + str(value) + suit + ".jpg"

	 suit_master = ["hearts", "spades", "clubs", "diamonds"]
	 value_master = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	 #where should card_position be stored? it's dependent upon the instance of the main stage (specific
	 #game) player obj..?
	 card_position = [(500, 500), (500, 100), (400, 500), (400, 100)]

	 def establish_image(self):
	 	image = pygame.image.load("cards/" + self.img).convert()
	 	image = Img(image, 400, 0)
	 	return image

class Deck:
	def __init__(self):
		self.cards = []
		self.create()

	def create(self):
		#for item in range(number_of_decks):
		for val in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
			for suit_elem in ["Hearts", "Spades", "Clubs", "Diamonds"]:
				self.cards.append(Card(val, suit_elem))

	def deal_hand(self):
		if len(self.cards) <= 4:
			return 0
		else:
			card_list, i = [], 0
			index_range = len(self.cards) - 1
			while i <= 3:
				n = random.randint(0, index_range - i)
				card_list.append(self.cards.pop(n))
				i += 1
			return card_list

	def deal_visual(self, n):
		flag = False
		if isinstance(n, Card):
			single_card = n.establish_image()
			return single_card
		else:
			return flag


deck1 = Deck()
card_list1 = deck1.deal_hand()


# for elem in card_list1:
# 	print(deal_visual(elem))

class Player:
	def __init__(self):
		self.cards = []
		self.score = 0





