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
			dx, dy = -1, -1
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


