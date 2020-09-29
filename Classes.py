import sys, pygame, random, math
from pygame.locals import *
import pygame_gui
# from Deck import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Img:
	def __init__(self, obj, x, y):
		self.obj = obj
		self.x = x
		self.y = y

	def move(fill_func, blit_func, screen_update_func,
	 screen_obj, second_obj):
	#for second_obj, could pass array of stage Img objs before updating the screen
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
				if isinstance(second_obj, list):
					for elem in second_obj:
						blit_func(elem.img.obj, (elem.img.x, elem.img.y))
				else:
					blit_func(second_obj.obj, (second_obj.x, second_obj.y))
			screen_update_func()
			return (self.x, self.y)
		return move_func
			

	def update_location(self, new_x, new_y):
		self.x, self.y = new_x, new_y



class Text(Img):
	def __init__(self, text, x, y):
		self.text = text
		self.x = x
		self.y = y
		super().__init__(self)
		self.obj = self.create_text_obj()


	def create_text_obj(self):
		font_obj = pygame.font.Font('fixedsys.ttf', 24)
		text_obj = font_obj.render(self.text, True, BLACK, WHITE)
		return text_obj




class Card:
	 def __init__(self, value, suit):  
	
	 	self.value = value
	 	self.suit = suit
	 	#make the object attribute store its own Img object (right?)
	 	#try rewriting w/ pygame.image.load("string.type").convert()
	 	self.img = self.establish_image()

	 suit_master = ["hearts", "spades", "clubs", "diamonds"]
	 value_master = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	 #where should card_position be stored? it's dependent upon the instance of the main stage (specific
	 #game) player obj..?
	 

	 def establish_image(self):
	 	image_construct = pygame.image.load("cards/" + 'f' + str(self.value) + self.suit + ".jpg").convert()
	 	image = Img(image_construct, 350, 0) #change for animation
	 	return image


class Deck:
	def __init__(self):
		self.cards = []
		self.position = -1
		self.create()
	

	def create(self):
		#for item in range(number_of_decks):
		for val in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
			for suit_elem in ["Hearts", "Spades", "Clubs", "Diamonds"]:
				self.cards.append(Card(val, suit_elem))

	def deal_card(self):
		if len(self.cards) == 0:
			return 0
		else:
			n = random.randint(0, (len(self.cards) - 1))
			new_card = self.cards.pop(n)
			self.position += 1
			return new_card

#rewrite, the move function is throwing a Nonetype error that's not worth unraveling
	def deal_visual(move, position_array):
		def deal_visual_func(self, n_card):
			# move1 = Img.move(screen.fill, screen.blit, pygame.display.update, WHITE, None)
			if isinstance(n_card, Card):
				single_card = n_card.establish_image()
				move(single_card, position_array[self.position][0], position_array[self.position][1])
				self.position += 1




class Player:
	def __init__(self):
		self.cards = []
		self.score = 0

	def update_score(self):
		if len(self.cards) == 0:
			self.score = 0
			return 0
		else:
			sum = 0
			for item in self.cards:
				if item.value <= 10:
					sum += item.value
				elif item.value == 14:
					if sum > 10:
						sum += 1
					else:
						sum += 11
				else:
					sum += 10
			self.score = sum
			return sum





