import sys, pygame, random
from pygame.locals import *
import pygame_gui
from Classes import Img, Deck, Player, Card

#screen set up

pygame.init()

pygame.display.set_caption('Blackjack (Rough Draft)')

#need to divide this up into classses

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
img_intro_text = Img(text_surface_obj, 60, 70)

font_obj_2 = pygame.font.Font('fixedsys.ttf', 24)
text_surface_obj_2 = font_obj_2.render('Press "h" to hold or "s" to stand for your turn', True, BLACK, WHITE)
text_surface_obj_3 = font_obj_2.render("The house will hit until their score is 17 or higher",
	True, BLACK, WHITE)
text_surface_obj_4 = font_obj_2.render("First to get a total score of 21 wins", True, BLACK, WHITE)
text_surface_obj_5 = font_obj_2.render("Past 21 is a bust, a tied score is a draw", True, BLACK, WHITE)
text_surface_obj_6 = font_obj_2.render("Good Luck", True, BLACK, WHITE)
cont_surface_obj = font_obj_2.render("(press Enter to continue or B to go back)", True, BLACK, WHITE)

instruct_text0 = Img(text_surface_obj_2, 75, 100) #coordinate fix
instruct_text1 = Img(text_surface_obj_3, 75, 100)
instruct_text2 = Img(text_surface_obj_4, 75, 100)
instruct_text3 = Img(text_surface_obj_5, 75, 100)
instruct_text4 = Img(text_surface_obj_6, 75, 100)
cont_text = Img(cont_surface_obj, 160, 400)

# text_rect_obj = text_surface_obj.get_rect()
# text_rect_obj.center = (400, 100)

#assign images

img_temp = pygame.image.load("graphics/pixel_pig.jpg").convert()
img0 = Img(img_temp, 400.0, 500.0)

# button set up
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (150, 50)),
 	text='Start', manager=manager)


#intro stage bool
intro = True
instruct = False
instruct_index = 0
main = False

#event [while] loop
while is_running:
	time_delta = clock.tick(60)/1000.0


	# for event in pygame.event.get():
	# 	if event.type == pygame.QUIT:
	# 		is_running = False

	# 	if event.type == pygame.USEREVENT:
	# 		if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
	# 			if event.ui_element == hello_button:
	# 				print('Hello World!')
	# 				print(hello_button.check_pressed())
	# 				intro = False
	# 				main = True
	# 				img0.x, img0.y = 800, 600
	# 				screen.fill(WHITE)
	# 				screen.blit(background, (0, 0))
	# 				pygame.display.update()
		
	# 	manager.process_events(event)

	manager.update(time_delta)
	
	while intro:
		
		manager.draw_ui(screen)
		move0 = Img.move(screen.fill, screen.blit, pygame.display.update, WHITE, img_intro_text)
		move0(img0, 40.0, 100.0)
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro, is_running = False, False
			if event.type == pygame.USEREVENT:
				if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
					screen.fill(WHITE)
					pygame.display.update()
					instruct = True
					intro = False
		manager.process_events(event)
		manager.update(time_delta)
		pygame.display.update()

	while instruct:
		screen.fill(WHITE)
		instruct_img_array = [instruct_text0, instruct_text1, instruct_text2, instruct_text3,
		instruct_text4] #orders the text images
		

		screen.blit(instruct_img_array[instruct_index].obj, (instruct_img_array[instruct_index].x,
		 instruct_img_array[instruct_index].y))
		screen.blit(cont_text.obj, (cont_text.x, cont_text.y))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				instruct, is_running = False, False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP_ENTER:
					if instruct_index < len(instruct_img_array) - 1:
						instruct_index += 1
						pygame.display.update()
					else:
						main = True
						instruct = False
				if event.key == pygame.K_b:
					if instruct_index > 0:
						instruct_index -= 1
						pygame.display.update()
					else:
						instruct_index = 0
						pygame.display.update()
			
		manager.process_events(event)
		manager.update(time_delta)


		pygame.display.update()


	while main:
		screen.fill(WHITE)
		#add conditional func so array is self-updating w/ more positions
		#what's the max possible number of hands?
		card_position = [(500, 500), (500, 100), (400, 500), (400, 100)]
		
		deck1 = Deck()
		initial_hand = deck1.deal_hand()
		temp = initial_hand[0]
		move0 = Img.move(screen.fill, screen.blit, pygame.display.update, WHITE, None)
		initial_animation = deck1.deal_visual(move0, card_position) #throwing an argument error
		#might be good idea to import global variables from Deck and update within Classes
		temp0 = initial_animation(temp)
	

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				main, is_running = False, False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP_ENTER:
					#UGH so tired. iron this out.
					print(isinstance(temp, Card))
			
		manager.process_events(event)
		manager.update(time_delta)


		pygame.display.update()

	
	pygame.display.update()
