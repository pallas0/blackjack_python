import sys, pygame, random
from pygame.locals import *
import pygame_gui

#screen set up

pygame.init()

pygame.display.set_caption('Blackjack (Rough Draft)')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

clock = pygame.time.Clock()
is_running = True

manager = pygame_gui.UIManager((800, 600))

#text setting
font_obj = pygame.font.Font('fixedsys.ttf', 64)
text_surface_obj = font_obj.render('pixel pig blackjack', True, BLACK, WHITE)
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (400, 100)

#assign images

img0 = pygame.image.load("graphics/pixel_pig.jpg").convert()
img0_x = 400
img0_y = 500

# button set up
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (150, 50)),
 	text='Start', manager=manager)

# goodbye_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 375), (100, 50)),
# 	text='Say Goodbye', manager=manager)


#event [while] loop

while is_running:
	time_delta = clock.tick(60)/1000.0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False

		if event.type == pygame.USEREVENT:
			if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
				if event.ui_element == hello_button:
					print('Hello World!')
					hello_button.hide()
		
		manager.process_events(event)

	manager.update(time_delta)

	if img0_x != 40:
		img0_x -= 4
		if img0_y != 100:
			img0_y -= 4
			screen.fill(WHITE)

	

	screen.blit(img0, (img0_x, img0_y))
	screen.blit(text_surface_obj, text_rect_obj)
	manager.draw_ui(screen)

	
	pygame.display.update()

# size = width, height = 940, 720
# speed = [1, 1]
# black = 0, 0, 0

# screen = pygame.display.set_mode(size)



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


#deck_test = Deck()


#n = random.randint(1, 54)


# obj = Card(14, "Clubs")
# obj_card = 'cards/' + obj.img + '.jpg'


# obj_img = pygame.image.load(obj_card)
# obj_rect = obj_img.get_rect()

# while 1:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT: sys.exit()

# 	obj_rect = obj_rect.move(speed)
# 	if obj_rect.left < 0 or obj_rect.right > width:
# 		speed[0] = -speed[0]
# 	if obj_rect.top < 0 or obj_rect.bottom > height:
# 		speed[1] = -speed[1]

# 	screen.fill(black)
# 	screen.blit(obj_img, obj_rect)
# 	pygame.display.flip()

#Card card = new Card(14, "clubs")

