import sys, pygame, random
from pygame.locals import *
pygame.init()

size = width, height = 940, 720
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

# obj_0 = Card(14, "clubs") #huh let's try that again. oh - not declared yet
#this needs to be a dictionary not an array/list
#wtf is the exact different between an array and a list again?
class Card:
	 def __init__(self, value, suit):  #ok apparently this is too old school.(args?)
	# on the upside,
	# it compiled! [and which friggin call is prompting that message? shall find out -.-]
	 	self.value = value
	 	self.suit = suit
	 	self.img = 'f' + str(value) + suit #jpg_images["f""{value}{suit}"] don't really need a dictionary unless there's a key val relationship
	 	#can create that if necessary, right now just using string
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

deck_test = Deck()
#lets_see = len(deck_test.cards)
lets_see = deck_test.cards[5]
img_check = lets_see.img
n = random.randint(1, 54)
print(n)
#Deck[0] == f2hearts
#cool. maybe I'm not a moron ^.^

obj = Card(14, "Clubs")
obj_card = 'cards/' + obj.img + '.jpg'

#VICTORY

obj_img = pygame.image.load(obj_card)
obj_rect = obj_img.get_rect()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	obj_rect = obj_rect.move(speed)
	if obj_rect.left < 0 or obj_rect.right > width:
		speed[0] = -speed[0]
	if obj_rect.top < 0 or obj_rect.bottom > height:
		speed[1] = -speed[1]

	screen.fill(black)
	screen.blit(obj_img, obj_rect)
	pygame.display.flip()

#Card card = new Card(14, "clubs")

